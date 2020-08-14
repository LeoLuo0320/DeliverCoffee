from .env import Env
from .office1 import Office1
from .office2 import Office2


def catalog(config) -> object:
    return {
        ('office', 'robot1'): Office1,
        ('office', 'robot2'): Office2,
    }[(config.domain_name, config.hardware_name)]()

