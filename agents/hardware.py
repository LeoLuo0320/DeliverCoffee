from tdict import Tdict

import hws
from agents import hierarchy


class HardwareAgent(hierarchy.HierarchicalAgent):
    def __init__(self, config):
        super().__init__()
        hw = hws.catalog(Tdict(hardware_name=config.hardware_name))
        self.skill_set.update(hw.skill_set)
