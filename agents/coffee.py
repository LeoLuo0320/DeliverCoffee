from . import hardware
from . import hierarchy


class CoffeeAgent(hardware.HardwareAgent):
    def __init__(self, config):
        super().__init__(config)
        self.domain_name = config.domain_name
        self.task_name = config.task_name

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
