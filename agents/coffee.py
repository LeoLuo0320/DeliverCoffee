from . import hardware
from . import hierarchy
from utils import DictTree
from envs.office1 import Office1

class CoffeeAgent(hardware.HardwareAgent):
    def __init__(self, config):
        super().__init__(config)
        self.domain_name = config.domain_name
        self.task_name = config.task_name

    def get_skillset(self):
        to_return = DictTree({skill.__name__: DictTree(
            step=None,
            model_name=getattr(skill_class, 'model_name', "log_poly2"),
            arg_in_len=skill_class.arg_in_len,
            max_cnt=getattr(skill_class, 'max_cnt', None),
            sub_skill_names=getattr(skill_class, 'sub_skill_names', []),
            ret_out_len=skill_class.ret_out_len,
            min_valid_data=getattr(skill_class, 'min_valid_data', None),
            sub_arg_accuracy=getattr(skill_class, 'sub_arg_accuracy', None),
        ) for skill, skill_class in list(self.skill_set.items()) + list(Office1.action_set)})

        for skill in to_return.values():
            if skill.sub_skill_names:
                skill.ret_in_len = max(to_return[sub_skill_name].ret_out_len for sub_skill_name in skill.sub_skill_names)
                skill.arg_out_len = max(skill.ret_out_len, max(to_return[sub_skill_name].arg_in_len for sub_skill_name in skill.sub_skill_names))
        # if config.rollable and not config.teacher:
        #     for skill_name, skill in self.skillset.items():
        #         if skill.sub_skill_names:
        #             skill.step = load_skill(config.model_dirname, skill_name, skill)
        self.stack = None
        self.last_act_name = None

        return to_return

    @property
    def root_skill_name(self):
        return 'DeliverCoffee'

    class DeliverCoffee(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['GetCoffee', 'DropOffCoffee']
        ret_out_len = 1

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: None
                ret_val: after DropOffCoffee -> True or False
            """
            if ret_name is None:
                return 'GetCoffee', None
            elif ret_name == 'GetCoffee' and ret_val == [True]:
                return 'DropOffCoffee', None
            elif ret_name == 'DropOffCoffee' and ret_val == [True]:
                return None, [True]
            else:
                return None, [False]

    class GetCoffee(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['MoveToCoffee', 'PickUpCoffee']
        ret_out_len = 1 #LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: None
                ret_val: after PickUpCoffee -> True or False that coffee has been picked up successfully
            """
            if ret_name is None:
                return 'MoveToCoffee', None
            elif ret_name == 'MoveToCoffee' and ret_val == [True]:
                return 'PickUpCoffee', None
            elif ret_name == 'PickUpCoffee' and ret_val == [True]:
                return None, [True]
            else:
                return None, [False]

    class MoveToCoffee(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['MoveToPosition']
        ret_out_len = 1 #LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: coffee
                ret_val: after MoveToPosition -> True or False if moved to coffee position
            """
            if ret_name is None:
                return 'MoveToPosition', [0]
            elif ret_name == 'MoveToPosition' and ret_val == [True]:
                return None, [True]
            else:
                return None, [False]

    class PickUpCoffee(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['Grasp']
        ret_out_len = 1  # LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: coffee
                ret_val: after Grasp -> True or False if grasp was successful
            """
            if cnt < 5 and ret_val is None:
                return 'Grasp', [0]
            elif ret_val == [True]:
                return None, [True]
            else:
                return None, [False]

    class DropOffCoffee(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['PlaceCoffee', 'MoveToOffice']
        ret_out_len = 1  # LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: None
                ret_val: after PlaceCoffee -> True or False that coffee has been placed down successfully
            """
            if ret_name is None:
                return 'MoveToOffice', None
            elif ret_name == 'MoveToOffice' and ret_val == [True]:
                return 'PlaceCoffee', None
            elif ret_name == 'PlaceCoffee' and ret_val == [True]:
                return None, [True]
            else:
                return None, [False]

    class MoveToOffice(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['MoveToPosition']
        ret_out_len = 1  # LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: None
                ret_val: after MoveToPosition -> True or False if moved to office position
            """
            if ret_name is None:
                return 'MoveToPosition', [1]
            elif ret_name == 'MoveToPosition' and ret_val == [True]:
                return None, [True]
            else:
                return None, [False]

    class PlaceCoffee(hierarchy.Skill):
        arg_in_len = 0
        sub_skill_names = ['Grasp']
        ret_out_len = 1  # LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: None
                ret_val: after Grasp -> True or False if grasp was successful
            """
            if ret_name is None:
                return 'Grasp', [1]
            elif ret_name == 'Grasp' and ret_val == [True]:
                return None, [True]
            else:
                return None, [False]
