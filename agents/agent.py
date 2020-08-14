import time

from tdict import Tdict


class Agent(object):
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
            trace.append(Tdict(
                timestamp=time.time(),
                act_name=act_name,
                act_arg=act_arg,
                info=info,
            ))
            if act_name is None:
                return trace

