import time

#from tdict import Tdict
from utils import DictTree

class Agent(object):
    def __init__(self, config):
        self.domain_name = config.domain_name
        self.task_name = config.task_name
    #
    # def __repr__(self):
    #     return self.task_name

    def reset(self, init_arg):
        raise NotImplementedError

    def step(self, obs):
        raise NotImplementedError

    def rollout(self, env):
        obs = None
        trace = []
        while True:
            act_name, act_arg, info = self.step(obs)
            if act_name is not None:
                obs = env.step(act_name, act_arg)
            trace.append(DictTree(
                timestamp=time.time(),
                act_name=act_name,
                act_arg=act_arg,
                info=info,
            ))
            if act_name is None:
                return trace

