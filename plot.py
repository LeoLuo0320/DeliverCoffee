import math
import pickle
import sys
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


BLACK = np.asarray([0, 0, 0], dtype=int)
PURPLE = np.asarray([226, 106, 179], dtype=int)
GREEN = np.asarray([65, 191, 112], dtype=int)
WHITE = np.asarray([255, 255, 255], dtype=int)
YELLOW = np.asarray([242, 226, 46], dtype=int)

NODES = {
    'DeliverCoffee': [80, 370, PURPLE, 'Deliver Coffee'],
    'GetCoffee': [150, 240, PURPLE, 'Get\nCoffee'],
    'DropOffCoffee': [160, 470, PURPLE, 'Drop off\nCoffee'],
    'MoveToCoffee': [280, 70, PURPLE, 'Move to\n Coffee'],
    'MoveToOffice': [280, 390, PURPLE, 'Move to\nOffice'],
    'PickUpCoffee': [280, 200, PURPLE, 'Pickup\nCoffee'],
    'PlaceCoffee': [280, 540, PURPLE, 'Place\nCoffee'],
    'MoveToPosition': [380, 270, GREEN, 'Move to\nPosition'],
    'Grasp': [380, 470, GREEN, 'Grasp'],
    'ObserveEnv': [540, 170, YELLOW, 'Observe\nEnvironment'],
    'Move': [540, 320, YELLOW, 'Move'],
    'ObservePick': [540, 470, YELLOW, 'Observe\nPick Up'],
    'ObserveDrop': [540, 620, YELLOW, 'Observe\nDrop Off'],
}

EDGES = {
    ('DeliverCoffee', 'GetCoffee'),
    ('DeliverCoffee', 'DropOffCoffee'),
    ('GetCoffee', 'MoveToCoffee'),
    ('GetCoffee', 'PickUpCoffee'),
    ('DropOffCoffee', 'PlaceCoffee'),
    ('DropOffCoffee', 'MoveToOffice'),
    ('MoveToCoffee', 'MoveToPosition'),
    ('MoveToOffice', 'MoveToPosition'),
    ('PickUpCoffee', 'Grasp'),
    ('PlaceCoffee', 'Grasp'),
    ('MoveToPosition', 'ObserveEnv'),
    ('MoveToPosition', 'Move'),
    ('Grasp', 'ObservePick'),
    ('Grasp', 'ObserveDrop'),
}


def make_hierarchy_video(fn_in, fn_out):
    width = 1280
    height = 720
    FPS = 30

    # v_out = cv2.VideoWriter(fn_out, cv2.VideoWriter_fourcc(*'mp4v'), float(FPS), (width, height))
    # v_out = cv2.VideoWriter(fn_out, cv2.VideoWriter_fourcc(*'MP42'), float(FPS), (width, height))

    trace = pickle.load(open(fn_in, 'rb'))

    stack = []
    popped_action = False

    for time_step_idx, time_step in enumerate(trace):
        skill_step_idx = 0
        while skill_step_idx < len(time_step.info.steps):
            skill_step = time_step.info.steps[skill_step_idx]
            if skill_step_idx == 0 and not popped_action:
                if time_step_idx == 0:
                    if skill_step.sub_name == time_step.act_name:
                        if stack[-1] == skill_step.name:
                            stack.append(time_step.act_name)
                    else:
                        stack.append(skill_step.name)
                else:
                    stack.pop()
                popped_action = True
                skill_step_idx -= 1
            elif skill_step.sub_name is None:
                stack.pop()
            else:
                stack.append(skill_step.sub_name)
                popped_action = False

            frame = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            frame[:, :width] = np.asarray([255, 255, 255], dtype=int)

            for name, node in NODES.items():
                if name in stack:
                    continue
                pos = [node[0] - 27, node[0] + 27, node[1] - 48, node[1] + 48]
                rounded_rectangle(
                    frame, (pos[2], pos[0]), (pos[3] - 1, pos[1] - 1), faded(node[2]), faded(BLACK), 10, 2)
                frame = centered_text(frame, node[3], (node[0], node[1]), faded(BLACK))

            for (name1, name2) in EDGES:
                if (name1, name2) in [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)]:
                    continue
                arrow(frame, (NODES[name1][0] + 25, NODES[name1][1] + 10), (NODES[name2][0] - 27, NODES[name2][1]),
                      faded(BLACK))

            for name, node in NODES.items():
                if name not in stack:
                    continue
                pos = [node[0] - 27, node[0] + 27, node[1] - 48, node[1] + 48]
                rounded_rectangle(frame, (pos[2], pos[0]), (pos[3] - 1, pos[1] - 1), node[2], BLACK, 10, 2)
                frame = centered_text(frame, node[3], (node[0], node[1]), BLACK)

            for (name1, name2) in EDGES:
                if (name1, name2) not in [(stack[i], stack[i + 1]) for i in range(len(stack) - 1)]:
                    continue
                arrow(frame, (NODES[name1][0] + 25, NODES[name1][1] + 10), (NODES[name2][0] - 27, NODES[name2][1]),
                      BLACK)

            skill_step_idx += 1

            for _ in range(30):
                v_out.write(frame)

    v_out.release()
    cv2.destroyAllWindows()


def rounded_rectangle(frame, top_left, bottom_right, fill_color, border_color, radius, thickness):
    top, left = top_left
    bottom, right = bottom_right

    fill_color0 = int(fill_color[0])
    fill_color1 = int(fill_color[1])
    fill_color2 = int(fill_color[2])
    fill_color_list = [fill_color0, fill_color1, fill_color2]

    border_color0 = int(border_color[0])
    border_color1 = int(border_color[1])
    border_color2 = int(border_color[2])
    border_color_list = [border_color0, border_color1, border_color2]

    cv2.rectangle(frame, (top, left + radius), (bottom, right - radius), fill_color_list, -1)
    cv2.rectangle(frame, (top + radius, left), (bottom - radius, right), fill_color_list, -1)
    cv2.line(frame, (top, left + radius), (top, right - radius), border_color_list, thickness)
    cv2.ellipse(frame, (top + radius, left + radius), (radius, radius), 180, 0, 90, fill_color_list, -1)
    cv2.ellipse(frame, (top + radius, left + radius), (radius, radius), 180, 0, 90, border_color_list, thickness)
    cv2.line(frame, (top + radius, left), (bottom - radius, left), border_color_list, thickness)
    cv2.ellipse(frame, (bottom - radius, left + radius), (radius, radius), 180, 90, 180, fill_color_list, -1)
    cv2.ellipse(frame, (bottom - radius, left + radius), (radius, radius), 180, 90, 180, border_color_list, thickness)
    cv2.line(frame, (bottom, left + radius), (bottom, right - radius), border_color_list, thickness)
    cv2.ellipse(frame, (bottom - radius, right - radius), (radius, radius), 180, 180, 270, fill_color_list, -1)
    cv2.ellipse(frame, (bottom - radius, right - radius), (radius, radius), 180, 180, 270, border_color_list, thickness)
    cv2.line(frame, (top + radius, right), (bottom - radius, right), border_color_list, thickness)
    cv2.ellipse(frame, (top + radius, right - radius), (radius, radius), 180, 270, 360, fill_color_list, -1)
    cv2.ellipse(frame, (top + radius, right - radius), (radius, radius), 180, 270, 360, border_color_list, thickness)


def faded(color, alpha=0.30):
    return (alpha * color + (1. - alpha) * np.asarray([255, 255, 255])).astype(np.int)


def centered_text(frame, text, box_center, color):
    font = ImageFont.truetype('helveticaneue.ttf', 16)
    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    line_h = box_center[0] - 20
    for line in text.split('\n'):
        w, h = draw.textsize(line, font=font)
        draw.text((box_center[1] + (200 - w) / 2 - 100, line_h), line, font=font, fill=tuple(color))
        line_h += h + 5
    return np.array(frame)


def arrow(frame, pos1, pos2, color):
    head_size = 15.
    head_angle = .4
    color0 = int(color[0])
    color1 = int(color[1])
    color2 = int(color[2])
    color_list = [color0, color1, color2]
    cv2.line(frame, (pos1[1], pos1[0]), (pos2[1], pos2[0]), color_list, 2)
    theta = math.atan((pos2[1] - pos1[1] + 0.) / (pos2[0] - pos1[0]))
    cv2.line(frame, (
        int(pos2[1] - head_size * math.sin(theta + head_angle)),
        int(pos2[0] - head_size * math.cos(theta + head_angle))),
             (pos2[1], pos2[0]), color_list, 2)
    cv2.line(frame, (
        int(pos2[1] - head_size * math.sin(theta - head_angle)),
        int(pos2[0] - head_size * math.cos(theta - head_angle))),
             (pos2[1], pos2[0]), color_list, 2)
