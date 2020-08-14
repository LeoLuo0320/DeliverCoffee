from tdict import Tdict

import utils
from . import agent


class Skill(object):
    @staticmethod
    def step(arg, cnt, ret_name, ret_val):
        raise NotImplementedError


class HierarchicalAgent(agent.Agent, metaclass=utils.subclass_set(Skill, 'skill_set')):
    """
    @DynamicAttrs
    """

    def __init__(self):
        self.stack = None
        self.last_act_name = None

    @property
    def root_skill_name(self):
        raise NotImplementedError

    def reset(self, init_arg):
        self.stack = [Tdict(name=self.root_skill_name, arg=init_arg, cnt=0)]
        self.last_act_name = None

    def step(self, obs):
        ret_name = self.last_act_name
        ret_val = obs

        steps = []
        while self.stack:
            top = self.stack[-1]
            sub_name, sub_arg = self.skill_set[top.name].step(top.arg, top.cnt, ret_name, ret_val)
            steps.append(Tdict(
                name=top.name,
                arg=top.arg,
                cnt=top.cnt,
                ret_name=ret_name,
                ret_val=ret_val,
                sub_name=sub_name,
                sub_arg=sub_arg,
            ))
            print("{}({}, {}, {}, {}) -> {}({})".format(
                top.name, top.arg, top.cnt, ret_name, ret_val, sub_name, sub_arg))
            if sub_name is None:
                self.stack.pop()
                ret_name = top.name
                ret_val = sub_arg
            elif sub_name in self.skill_set:
                top.cnt += 1
                self.stack.append(Tdict(name=sub_name, arg=sub_arg, cnt=0))
                ret_name = None
                ret_val = None
            else:
                top.cnt += 1
                self.last_act_name = sub_name
                return sub_name, sub_arg, Tdict(steps=steps)
        self.last_act_name = None
        return None, None, Tdict(steps=steps)
