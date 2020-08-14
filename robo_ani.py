from tkinter import *
import time

HORIZONTAL_WALL = [
    (0, 3), (2, 3), (3, 3), (5, 3), (6, 3), (8, 3), (9, 3), (11, 3),
    (0, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (11, 6)
]

VERTICAL_WALL = [
    (2, 0), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 8),
    (5, 0), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 8),
    (8, 0), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 8)
]


def display_env(robot_name, moves_list):
    """
        robot_name: R1 or R2
        moves_list: list of moves and status of has coffee
    """
    master = Tk()
    gridworld = Canvas(master, width=900, height=800, borderwidth=1)
    gridworld.grid(row=1, column=0, sticky=E + W, columnspan=10, rowspan=10)

    COFFEE_POS = moves_list.pop()
    OFFICE_POS = moves_list.pop()
    ROBOT_NAME = robot_name

    if ROBOT_NAME == 1:
        ROBOT_NAME = "R1"
    elif ROBOT_NAME == 2:
        ROBOT_NAME = "R2"

    count = 0
    finished_moves = []

    while (count != len(moves_list)):
        for y in range(9):
            t = 0
            m = 70
            b = 70 * (y + 1)
            c = 70 * (y)
            for x in range(12):
                gridworld.create_rectangle(t, c, m, b, fill='white')

                mid_x = (t + m) / 2
                mid_y = (c + b) / 2

                if (x, y) in HORIZONTAL_WALL:
                    gridworld.create_line(t, c, m, c, width=5)
                if (x, y) in VERTICAL_WALL:
                    gridworld.create_line(m, c, m, b, width=5)

                if (x, y) == COFFEE_POS:
                    gridworld.create_text(mid_x, mid_y, text="C")

                if (x, y) == OFFICE_POS:
                    gridworld.create_text(mid_x, mid_y, text="O")

                if (x, y) in finished_moves:
                    gridworld.create_rectangle(t, c, m, b, fill='red')

                if (x, y) == moves_list[count][0]:
                    gridworld.create_text(mid_x, mid_y, text=robot_name)
                    finished_moves.append((x, y))

                if (x, y) == moves_list[count][0] and moves_list[count][1] is True:
                    gridworld.create_rectangle(t, c, m, b, fill='white')
                    gridworld.create_text(mid_x, mid_y, text=robot_name + "C")

                if (x, y) == COFFEE_POS == moves_list[count][0]:
                    gridworld.create_rectangle(t, c, m, b, fill='white')
                    gridworld.create_text(mid_x, mid_y, text=robot_name + "C")

                if (x, y) == OFFICE_POS == moves_list[count][0]:
                    gridworld.create_rectangle(t, c, m, b, fill='white')
                    gridworld.create_text(mid_x, mid_y, text=robot_name + "CO")

                t += 70
                m += 70

        count += 1
        time.sleep(.6)
        master.update()
    time.sleep(2)
