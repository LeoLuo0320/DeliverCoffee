import networkx as nx
import numpy as np
import random
from . import env

import pickle


class Office(env.Env):
    OFFICE_WIDTH = 12
    OFFICE_HEIGHT = 9
    ROBOT_INIT_POS = (random.randint(0,OFFICE_WIDTH-1), random.randint(0,OFFICE_HEIGHT-1))
    COFFEE_POS = (random.randint(0,OFFICE_WIDTH-1), random.randint(0,OFFICE_HEIGHT-1))
    OFFICE_POS = (random.randint(0,OFFICE_WIDTH-1), random.randint(0,OFFICE_HEIGHT-1))

    REFORM_GRIDY = {
        0: 8,
        8: 0,
        1: 7,
        7: 1,
        2: 6,
        6: 2,
        3: 5,
        5: 3,
        4: 4
    }

    OFFICE_G = nx.grid_2d_graph(OFFICE_WIDTH, OFFICE_HEIGHT)

    # Edges with attributes diagonal
    OFFICE_G.add_edge((0, 0), (1, 1), move="diagonal")
    OFFICE_G.add_edge((0, 1), (1, 2), move="diagonal")
    OFFICE_G.add_edge((0, 1), (1, 0), move="diagonal")
    OFFICE_G.add_edge((0, 2), (1, 3), move="diagonal")
    OFFICE_G.add_edge((0, 2), (1, 1), move="diagonal")
    OFFICE_G.add_edge((0, 3), (1, 4), move="diagonal")
    OFFICE_G.add_edge((0, 3), (1, 2), move="diagonal")
    OFFICE_G.add_edge((0, 4), (1, 5), move="diagonal")
    OFFICE_G.add_edge((0, 4), (1, 3), move="diagonal")
    OFFICE_G.add_edge((0, 5), (1, 6), move="diagonal")
    OFFICE_G.add_edge((0, 5), (1, 4), move="diagonal")
    OFFICE_G.add_edge((0, 6), (1, 7), move="diagonal")
    OFFICE_G.add_edge((0, 6), (1, 5), move="diagonal")
    OFFICE_G.add_edge((0, 7), (1, 8), move="diagonal")
    OFFICE_G.add_edge((0, 7), (1, 6), move="diagonal")
    OFFICE_G.add_edge((0, 8), (1, 7), move="diagonal")

    OFFICE_G.add_edge((1, 0), (2, 1), move="diagonal")
    OFFICE_G.add_edge((1, 1), (2, 2), move="diagonal")
    OFFICE_G.add_edge((1, 1), (2, 0), move="diagonal")
    OFFICE_G.add_edge((1, 2), (2, 3), move="diagonal")
    OFFICE_G.add_edge((1, 2), (2, 1), move="diagonal")
    OFFICE_G.add_edge((1, 3), (2, 4), move="diagonal")
    OFFICE_G.add_edge((1, 3), (2, 2), move="diagonal")
    OFFICE_G.add_edge((1, 4), (2, 5), move="diagonal")
    OFFICE_G.add_edge((1, 4), (2, 3), move="diagonal")
    OFFICE_G.add_edge((1, 5), (2, 6), move="diagonal")
    OFFICE_G.add_edge((1, 5), (2, 4), move="diagonal")
    OFFICE_G.add_edge((1, 6), (2, 7), move="diagonal")
    OFFICE_G.add_edge((1, 6), (2, 5), move="diagonal")
    OFFICE_G.add_edge((1, 7), (2, 8), move="diagonal")
    OFFICE_G.add_edge((1, 7), (2, 6), move="diagonal")
    OFFICE_G.add_edge((1, 8), (2, 7), move="diagonal")

    OFFICE_G.add_edge((2, 0), (3, 1), move="diagonal")
    OFFICE_G.add_edge((2, 1), (3, 2), move="diagonal")
    OFFICE_G.add_edge((2, 1), (3, 0), move="diagonal")
    OFFICE_G.add_edge((2, 2), (3, 1), move="diagonal")
    OFFICE_G.add_edge((2, 6), (3, 7), move="diagonal")
    OFFICE_G.add_edge((2, 7), (3, 8), move="diagonal")
    OFFICE_G.add_edge((2, 7), (3, 6), move="diagonal")
    OFFICE_G.add_edge((2, 8), (3, 7), move="diagonal")

    OFFICE_G.add_edge((3, 0), (4, 1), move="diagonal")
    OFFICE_G.add_edge((3, 1), (4, 2), move="diagonal")
    OFFICE_G.add_edge((3, 1), (4, 0), move="diagonal")
    OFFICE_G.add_edge((3, 2), (4, 1), move="diagonal")
    OFFICE_G.add_edge((3, 3), (4, 4), move="diagonal")
    OFFICE_G.add_edge((3, 4), (4, 5), move="diagonal")
    OFFICE_G.add_edge((3, 4), (4, 3), move="diagonal")
    OFFICE_G.add_edge((3, 5), (4, 6), move="diagonal")
    OFFICE_G.add_edge((3, 5), (4, 4), move="diagonal")
    OFFICE_G.add_edge((3, 6), (4, 7), move="diagonal")
    OFFICE_G.add_edge((3, 6), (4, 5), move="diagonal")
    OFFICE_G.add_edge((3, 7), (4, 8), move="diagonal")
    OFFICE_G.add_edge((3, 7), (4, 6), move="diagonal")
    OFFICE_G.add_edge((3, 8), (4, 7), move="diagonal")

    OFFICE_G.add_edge((4, 0), (5, 1), move="diagonal")
    OFFICE_G.add_edge((4, 1), (5, 2), move="diagonal")
    OFFICE_G.add_edge((4, 1), (5, 0), move="diagonal")
    OFFICE_G.add_edge((4, 2), (5, 1), move="diagonal")
    OFFICE_G.add_edge((4, 3), (5, 4), move="diagonal")
    OFFICE_G.add_edge((4, 4), (5, 5), move="diagonal")
    OFFICE_G.add_edge((4, 4), (5, 3), move="diagonal")
    OFFICE_G.add_edge((4, 5), (5, 6), move="diagonal")
    OFFICE_G.add_edge((4, 5), (5, 4), move="diagonal")
    OFFICE_G.add_edge((4, 6), (5, 7), move="diagonal")
    OFFICE_G.add_edge((4, 6), (5, 5), move="diagonal")
    OFFICE_G.add_edge((4, 7), (5, 8), move="diagonal")
    OFFICE_G.add_edge((4, 7), (5, 6), move="diagonal")
    OFFICE_G.add_edge((4, 8), (5, 7), move="diagonal")

    OFFICE_G.add_edge((5, 0), (6, 1), move="diagonal")
    OFFICE_G.add_edge((5, 1), (6, 2), move="diagonal")
    OFFICE_G.add_edge((5, 1), (6, 0), move="diagonal")
    OFFICE_G.add_edge((5, 2), (6, 1), move="diagonal")
    OFFICE_G.add_edge((5, 6), (6, 7), move="diagonal")
    OFFICE_G.add_edge((5, 7), (6, 8), move="diagonal")
    OFFICE_G.add_edge((5, 7), (6, 6), move="diagonal")
    OFFICE_G.add_edge((5, 8), (6, 7), move="diagonal")

    OFFICE_G.add_edge((6, 0), (7, 1), move="diagonal")
    OFFICE_G.add_edge((6, 1), (7, 2), move="diagonal")
    OFFICE_G.add_edge((6, 1), (7, 0), move="diagonal")
    OFFICE_G.add_edge((6, 2), (7, 1), move="diagonal")
    OFFICE_G.add_edge((6, 3), (7, 4), move="diagonal")
    OFFICE_G.add_edge((6, 4), (7, 5), move="diagonal")
    OFFICE_G.add_edge((6, 4), (7, 3), move="diagonal")
    OFFICE_G.add_edge((6, 5), (7, 6), move="diagonal")
    OFFICE_G.add_edge((6, 5), (7, 4), move="diagonal")
    OFFICE_G.add_edge((6, 6), (7, 7), move="diagonal")
    OFFICE_G.add_edge((6, 6), (7, 5), move="diagonal")
    OFFICE_G.add_edge((6, 7), (7, 8), move="diagonal")
    OFFICE_G.add_edge((6, 7), (7, 6), move="diagonal")
    OFFICE_G.add_edge((6, 8), (7, 7), move="diagonal")

    OFFICE_G.add_edge((7, 0), (8, 1), move="diagonal")
    OFFICE_G.add_edge((7, 1), (8, 2), move="diagonal")
    OFFICE_G.add_edge((7, 1), (8, 0), move="diagonal")
    OFFICE_G.add_edge((7, 2), (8, 1), move="diagonal")
    OFFICE_G.add_edge((7, 3), (8, 4), move="diagonal")
    OFFICE_G.add_edge((7, 4), (8, 5), move="diagonal")
    OFFICE_G.add_edge((7, 4), (8, 3), move="diagonal")
    OFFICE_G.add_edge((7, 5), (8, 6), move="diagonal")
    OFFICE_G.add_edge((7, 5), (8, 4), move="diagonal")
    OFFICE_G.add_edge((7, 6), (8, 7), move="diagonal")
    OFFICE_G.add_edge((7, 6), (8, 5), move="diagonal")
    OFFICE_G.add_edge((7, 7), (8, 8), move="diagonal")
    OFFICE_G.add_edge((7, 7), (8, 6), move="diagonal")
    OFFICE_G.add_edge((7, 8), (8, 7), move="diagonal")

    OFFICE_G.add_edge((8, 0), (9, 1), move="diagonal")
    OFFICE_G.add_edge((8, 1), (9, 2), move="diagonal")
    OFFICE_G.add_edge((8, 1), (9, 0), move="diagonal")
    OFFICE_G.add_edge((8, 2), (9, 1), move="diagonal")
    OFFICE_G.add_edge((8, 6), (9, 7), move="diagonal")
    OFFICE_G.add_edge((8, 7), (9, 8), move="diagonal")
    OFFICE_G.add_edge((8, 7), (9, 6), move="diagonal")
    OFFICE_G.add_edge((8, 8), (9, 7), move="diagonal")

    OFFICE_G.add_edge((9, 0), (10, 1), move="diagonal")
    OFFICE_G.add_edge((9, 1), (10, 2), move="diagonal")
    OFFICE_G.add_edge((9, 1), (10, 0), move="diagonal")
    OFFICE_G.add_edge((9, 2), (10, 3), move="diagonal")
    OFFICE_G.add_edge((9, 2), (10, 1), move="diagonal")
    OFFICE_G.add_edge((9, 3), (10, 4), move="diagonal")
    OFFICE_G.add_edge((9, 3), (10, 2), move="diagonal")
    OFFICE_G.add_edge((9, 4), (10, 5), move="diagonal")
    OFFICE_G.add_edge((9, 4), (10, 3), move="diagonal")
    OFFICE_G.add_edge((9, 5), (10, 6), move="diagonal")
    OFFICE_G.add_edge((9, 5), (10, 4), move="diagonal")
    OFFICE_G.add_edge((9, 6), (10, 7), move="diagonal")
    OFFICE_G.add_edge((9, 6), (10, 5), move="diagonal")
    OFFICE_G.add_edge((9, 7), (10, 8), move="diagonal")
    OFFICE_G.add_edge((9, 7), (10, 6), move="diagonal")
    OFFICE_G.add_edge((9, 8), (10, 7), move="diagonal")

    OFFICE_G.add_edge((10, 0), (11, 1), move="diagonal")
    OFFICE_G.add_edge((10, 1), (11, 2), move="diagonal")
    OFFICE_G.add_edge((10, 1), (11, 0), move="diagonal")
    OFFICE_G.add_edge((10, 2), (11, 3), move="diagonal")
    OFFICE_G.add_edge((10, 2), (11, 1), move="diagonal")
    OFFICE_G.add_edge((10, 3), (11, 4), move="diagonal")
    OFFICE_G.add_edge((10, 3), (11, 2), move="diagonal")
    OFFICE_G.add_edge((10, 4), (11, 5), move="diagonal")
    OFFICE_G.add_edge((10, 4), (11, 3), move="diagonal")
    OFFICE_G.add_edge((10, 5), (11, 6), move="diagonal")
    OFFICE_G.add_edge((10, 5), (11, 4), move="diagonal")
    OFFICE_G.add_edge((10, 6), (11, 7), move="diagonal")
    OFFICE_G.add_edge((10, 6), (11, 5), move="diagonal")
    OFFICE_G.add_edge((10, 7), (11, 8), move="diagonal")
    OFFICE_G.add_edge((10, 7), (11, 6), move="diagonal")
    OFFICE_G.add_edge((10, 8), (11, 7), move="diagonal")

    # Removed edges represent walls
    OFFICE_G.remove_edge((0, 2), (0, 3))
    OFFICE_G.remove_edge((0, 5), (0, 6))

    OFFICE_G.remove_edge((11, 2), (11, 3))
    OFFICE_G.remove_edge((11, 5), (11, 6))

    OFFICE_G.remove_edge((4, 2), (4, 3))
    OFFICE_G.remove_edge((7, 2), (7, 3))

    OFFICE_G.remove_edge((2, 2), (3, 2))
    OFFICE_G.remove_edge((2, 3), (3, 3))
    OFFICE_G.remove_edge((2, 4), (3, 4))
    OFFICE_G.remove_edge((2, 5), (3, 5))
    OFFICE_G.remove_edge((2, 6), (3, 6))
    OFFICE_G.remove_edge((2, 8), (3, 8))
    OFFICE_G.remove_edge((2, 2), (2, 3))
    OFFICE_G.remove_edge((3, 2), (3, 3))
    OFFICE_G.remove_edge((2, 5), (2, 6))
    OFFICE_G.remove_edge((3, 5), (3, 6))

    OFFICE_G.remove_edge((5, 0), (6, 0))
    OFFICE_G.remove_edge((5, 2), (6, 2))
    OFFICE_G.remove_edge((5, 3), (6, 3))
    OFFICE_G.remove_edge((5, 4), (6, 4))
    OFFICE_G.remove_edge((5, 5), (6, 5))
    OFFICE_G.remove_edge((5, 6), (6, 6))
    OFFICE_G.remove_edge((5, 8), (6, 8))
    OFFICE_G.remove_edge((5, 2), (5, 3))
    OFFICE_G.remove_edge((6, 2), (6, 3))
    OFFICE_G.remove_edge((5, 5), (5, 6))
    OFFICE_G.remove_edge((6, 5), (6, 6))

    OFFICE_G.remove_edge((8, 0), (9, 0))
    OFFICE_G.remove_edge((8, 2), (9, 2))
    OFFICE_G.remove_edge((8, 3), (9, 3))
    OFFICE_G.remove_edge((8, 4), (9, 4))
    OFFICE_G.remove_edge((8, 5), (9, 5))
    OFFICE_G.remove_edge((8, 6), (9, 6))
    OFFICE_G.remove_edge((8, 8), (9, 8))
    OFFICE_G.remove_edge((8, 2), (8, 3))
    OFFICE_G.remove_edge((9, 2), (9, 3))
    OFFICE_G.remove_edge((8, 5), (8, 6))
    OFFICE_G.remove_edge((9, 5), (9, 6))

    def __init__(self):
        self.robot_curr_pos = None
        self.has_coffee = None
        self.moves_list = []
        self.count = 0

    def reset(self):
        self.robot_curr_pos = np.array(Office.ROBOT_INIT_POS)
        self.has_coffee = None
        self.moves_list = []
        self.count = 0

    def display_env_info(self, tf):
        """
            tf: 1 if on last move, 0 if not on last move
        """

        if self.robot_curr_pos[0] == self.OFFICE_POS[0] and self.robot_curr_pos[1] == self.OFFICE_POS[1] and tf:
            self.moves_list.append(
                [(self.robot_curr_pos[0], self.REFORM_GRIDY[self.robot_curr_pos[1]]), self.has_coffee])
            self.moves_list.append((self.OFFICE_POS[0], self.REFORM_GRIDY[self.OFFICE_POS[1]]))
            self.moves_list.append((self.COFFEE_POS[0], self.REFORM_GRIDY[self.COFFEE_POS[1]]))

            pickle.dump(self.moves_list, open("moves_list.pkl", 'wb'),
                        protocol=2)
        if self.count == 0:
            self.moves_list.append(
                [(self.ROBOT_INIT_POS[0], self.REFORM_GRIDY[self.ROBOT_INIT_POS[1]]), self.has_coffee])

        self.count += 1

        self.moves_list.append([(self.robot_curr_pos[0], self.REFORM_GRIDY[self.robot_curr_pos[1]]), self.has_coffee])

    class ObserveEnv(env.Action):
        arg_in_len = 1
        ret_out_len = 3

        @staticmethod
        def apply(e, arg):
            """
                arg: coffee or office
                ret_val: [coffee or office coordinates, robot current position coordinates, office graph]
            """
            # TODO: make arg numeric
            #assert arg in [[0], [1]]

            if arg == [0]:
                return [e.COFFEE_POS, tuple(e.robot_curr_pos), e.OFFICE_G]
            if arg == [1]:
                return [e.OFFICE_POS, tuple(e.robot_curr_pos), e.OFFICE_G]

    class Move(env.Action):
        arg_in_len = 3
        ret_out_len = 1

        @staticmethod
        def legal_move(e, move_to):
            if not tuple(np.asarray(move_to) - e.robot_curr_pos) in e.get_possible_move_list():
                return False
            elif not e.OFFICE_G.has_edge(tuple(e.robot_curr_pos), move_to):
                return False
            else:
                return True

        @staticmethod
        def apply(e, arg):
            """
                arg: coordinates to move to, final destination coordinates, robot_name
                ret_val: True or False if moved to final position yet
            """
            move_to = arg[0]
            fin_dest = arg[1]

            if tuple(e.robot_curr_pos) == fin_dest:
                e.display_env_info(0)
                return [True]
            elif Office.Move.legal_move(e, move_to):
                e.robot_curr_pos = np.asarray(move_to)
                e.display_env_info(1)
            else:
                return [False]
