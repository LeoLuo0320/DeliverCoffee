from agents import hierarchy
from hws import robot
import networkx as nx


class Robot2(robot.Robot):
    """
        Robot2 moves by going in any directions
    """

    @staticmethod
    def plan_path(fin_dest, curr_dest, G):
        curr_dest = tuple(curr_dest)
        path = nx.shortest_path(G, source=curr_dest, target=fin_dest)
        print("Planned path: ", path)
        if len(path) > 1:
            move_coords = path[1]
        else:
            move_coords = path[0]
        return move_coords

    class MoveToPosition(hierarchy.Skill):
        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: 0 or 1
                ret_val: after ObserveEnv -> [coffee or office coordinates, robot current pos coordinates, office graph]
                         after Move -> True or False
            """
            # if ret_name == 'Move' and ret_val == [True]:
            #     return None, [True]
            #
            # if cnt % 2 == 0 and ret_val != [True]:
            #     return 'ObserveEnv', arg
            # else:
            #     path = Robot2.MoveToPosition.plan_path(*ret_val)
            #     return 'Move', [path, ret_val[0], 2]
            #     # return 'Move', [path, ret_val[0], 'robot2']

            if ret_name in [None, 'Move']:
                if ret_val:
                    return None, [True]
                else:
                    return 'ObserveEnv', arg
            else:
                move_to = Robot2.plan_path(*ret_val)
                return 'Move', [move_to, ret_val[0], 2]

    class Grasp(hierarchy.Skill):
        @staticmethod
        def step(arg, cnt, ret_name, ret_val):
            """
                arg: 0 or 1
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
