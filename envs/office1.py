from . import office
from . import env


class Office1(office.Office):
    @classmethod
    def get_possible_move_list(cls):
        return {
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        }

    class ObservePick(env.Action):
        @staticmethod
        def apply(e, arg):
            if arg == [0]:
                if not e.has_coffee:
                    if tuple(e.robot_curr_pos) == e.COFFEE_POS:
                        e.has_coffee = True
                        return [True]

            else:
                return [False]

    class ObserveDrop(env.Action):
        @staticmethod
        def apply(e, arg):
            if arg == [1]:
                if e.has_coffee:
                    if tuple(e.robot_curr_pos) == e.OFFICE_POS:
                        e.has_coffee = False
                        return [True]
            else:
                return [False]
