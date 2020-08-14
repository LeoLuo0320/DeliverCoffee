from .robot1 import Robot1
from .robot2 import Robot2


def catalog(config):
    return {
        'robot1': Robot1,
        'robot2': Robot2,
    }[config.hardware_name]()
