from agents import hierarchy
from hws import robot
from envs import office
import networkx as nx


class Robot1(robot.Robot):
    """
        Robot1 moves only by going in 4 directions
    """

    # @staticmethod
    # def plan_path(fin_dest, curr_dest, g):
    #     curr_dest = tuple(curr_dest)
    #     h = g.copy()
    #     edges_to_remove = [edge for edge in h.edges(data=True) if (h.get_edge_data(*edge))]
    #     h.remove_edges_from(edges_to_remove)
    #     path = nx.shortest_path(h, source=curr_dest, target=fin_dest)
    #     if len(path) > 1:
    #         move_coords = path[1]
    #     else:
    #         move_coords = path[0]
    #     return move_coords

    class MoveToPosition(hierarchy.Skill):

        arg_in_len = 1
        sub_skill_names = ['ObserveEnv', 'Move', 'PlanPath']
        ret_out_len = 1  # LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: coffee or office
                ret_val: after ObserveEnv -> [coffee or office coordinates, robot current pos coordinates, office graph]
                         after Move -> True or False
            """
            if ret_name in [None, 'Move']:
                if ret_val:
                    return None, [True]
                else:
                    return 'ObserveEnv', arg
            elif ret_name == 'ObserveEnv':
                return 'PlanPath', [0]+ret_val
            elif ret_name == 'PlanPath':
                #move_to = Robot1.plan_path(*ret_val)
                return 'Move', ret_val + [1]

    class Grasp(hierarchy.Skill):
        arg_in_len = 1
        sub_skill_names = ['ObservePick', 'ObserveDrop']
        ret_out_len = 1  # LeoLuo

        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: coffee or office
                ret_val: after ObserveEnv -> [coffee or office coordinates, robot current pos coordinates, office graph]
                         after -> True or False if at correct position and performed "grasp"
            """
            if ret_val == [True] and ret_name in ['ObservePick', 'ObserveDrop']:
                return None, [True]
            elif arg == [0] and ret_val is None:
                return 'ObservePick', arg
            elif arg == [1] and ret_val is None:
                return 'ObserveDrop', arg
            else:
                return None, [False]

            # if cnt == 0:
            #     return 'ObserveEnv', arg
            # else:
            #     ret_v = tuple(ret_val[1])
            #     if ret_val[0] == ret_v:
            #         print("Successful Robot1 Grasp")
            #         return None, True
            #     else:
            #         return None, False
