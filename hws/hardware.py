import utils
import networkx as nx
from agents import hierarchy


class Hardware(object, metaclass=utils.subclass_set(hierarchy.Skill, 'skill_set')):

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

    pass