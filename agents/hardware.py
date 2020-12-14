#from tdict import Tdict
from utils import DictTree
import hws
from agents import hierarchy


class HardwareAgent(hierarchy.HierarchicalAgent):
    def __init__(self, config):
        super().__init__(config)
        hw = hws.catalog(DictTree(hardware_name=config.hardware_name))
        self.skill_set.update(hw.skill_set)
        #self.domain_name = config.domain_name
        #self.task_name = config.task_name
