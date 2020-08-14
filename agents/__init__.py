from .coffee import CoffeeAgent
from .hardware import HardwareAgent
from .hierarchy import HierarchicalAgent


def catalog(config):
    return {
        'coffee': CoffeeAgent,
    }[config.task_name](config)
