# Hardware-Aware Hierarchical Control

**To run:**\
`python main.py --domain office --task coffee --hardware robot1`\
`python main.py --domain office --task coffee --hardware robot2`

**To see display of robot moving through gridworld:**\
    In main.py, uncomment lines:\
        `moves_list = pickle.load(open("moves_list.pkl", 'rb'))`\
        `robo_ani.display_env(args.hardware, moves_list)`\
    In office.py, uncomment lines:\
        `e.display_env_info(0)`\
        `e.display_env_info(1)`


**To produce a .mp4 file of skill hierarchy:**\
  In main.py, uncomment line:\
    `plot.make_hierarchy_video("trace_result.pkl", "plot_output.mp4")`\
  In plot.py, uncomment line:\
    `v_out = cv2.VideoWriter(fn_out, cv2.VideoWriter_fourcc(*'mp4v'), float(FPS), (width, height))`

**To produce a .avi file of skill hierarchy:**\
  In main.py, uncomment line:\
    `plot.make_hierarchy_video("trace_result.pkl", "./plot_out.avi")`\
  In plot.py, uncomment line:\
    `v_out = cv2.VideoWriter(fn_out, cv2.VideoWriter_fourcc(*'MP42'), float(FPS), (width, height))`
