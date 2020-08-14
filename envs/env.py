import utils


class Action(object):
    @staticmethod
    def apply(e, arg):
        raise NotImplementedError


class Env(metaclass=utils.subclass_set(Action, 'action_set')):
    """
    @DynamicAttrs
    """
    def reset(self):
        raise NotImplementedError

    def step(self, act_name, act_arg):
        return self.action_set[act_name].apply(self, act_arg)
