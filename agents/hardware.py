#from tdict import Tdict
from utils import DictTree
import hws
from agents import hierarchy
import pickle


class HardwareAgent(hierarchy.HierarchicalAgent):
    def __init__(self, config):
        super().__init__(config)
        print(f"HardwareAgent: {self.skill_set}")
        hw = hws.catalog(DictTree(hardware_name=config.hardware_name))
        self.skill_set.update(hw.skill_set)
        #self.domain_name = config.domain_name
        #self.task_name = config.

        self.skillset = dict(list(self.skill_set.items()) + list(self.actions.items()))
        for skill in list(self.skill_set.values()):
            if skill.sub_skill_names:
                skill.ret_in_len = max(
                    self.skillset[sub_skill_name].ret_out_len for sub_skill_name in skill.sub_skill_names)
                skill.arg_out_len = max(skill.ret_out_len, max(
                    self.skillset[sub_skill_name].arg_in_len for sub_skill_name in skill.sub_skill_names))
        if not(config.model_dirname is None): #and not config.teacher:
            print("Here")
            for skill_name, skill in self.skillset.items():
                if skill.sub_skill_names:
                    skill.step = self.load_skill(config.model_dirname, skill_name, skill)

    def load_skill(model_dirname, skill_name, skill):
        model = pickle.load(open("{}/{}.pkl".format(model_dirname, skill_name), 'rb'))

        def step(arg, cnt, ret_name, ret_val, obs):
            if arg is not None:
                assert not any(arg[skill.arg_in_len:])
                arg = arg[:skill.arg_in_len]
            if ret_val is not None:
                assert not any(ret_val[skill.ret_in_len:])
                ret_val = ret_val[:skill.ret_in_len]
            sub_skill_names = [None] + skill.sub_skill_names
            iput = (utils.pad(arg, skill.arg_in_len) + [cnt]
                    + utils.one_hot(sub_skill_names.index(ret_name), len(sub_skill_names))
                    + utils.pad(ret_val, skill.ret_in_len)
                    + obs)
            oput = model.predict([iput])
            sub_name = sub_skill_names[oput.sub[0]]
            sub_arg = list(oput.arg[0])
            if sub_name is None:
                return None, sub_arg
            else:
                assert not any(sub_arg[skill.arg_out_len:])
                sub_arg = sub_arg[:skill.arg_out_len]
                return sub_name, sub_arg

        return step
