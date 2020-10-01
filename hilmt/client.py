import json
import requests as req
import numpy as np
from utils import DictTree
import networkx as nx
from networkx.readwrite import json_graph

SERVER_URL = 'http://localhost:5000'


class MyEncoder(DictTree.JSONEncoder):
    def default(self, o):
        if isinstance(o, DictTree):
            return vars(o)
        elif isinstance(o, np.integer):
            return int(o)
        elif isinstance(o, np.floating):
            return float(o)
        elif isinstance(o, np.ndarray):
            return o.tolist()
        elif isinstance(o, nx.classes.graph.Graph):
            return json_graph.node_link_data(o)
        else:
            return super(DictTree.JSONEncoder, self).default(o)

def delete(agent):
    return DictTree(req.delete('{}/agent/{}/{}/'.format(SERVER_URL, agent.domain_name, agent.task_name)).json())


def register(agent):
    # Debugger
    # print("Debug Starts:")
    # for skill, skill_class in agent.get_skillset().items():
    #    print("Key is ", skill, ", Type is ", type(skill))
    #    print("Value is ", skill_class, ", Type is ", type(skill_class))

    data = json.dumps(agent.get_skillset(), cls=DictTree.JSONEncoder)
    # Debugger
    #print("Data is ", data)
    return DictTree(req.post('{}/agent/{}/{}/'.format(SERVER_URL, agent.domain_name, agent.task_name), data=data).json())


def train(agent, config):
    for k, v in config.items():
        print("Key is ", k)
        print("Value is ", v)
    data = json.dumps(config, cls=MyEncoder)
    return DictTree(req.put('{}/agent/{}/{}/'.format(SERVER_URL, agent.domain_name, agent.task_name), data=data).json())


def train_agent(agent, traces, config):
    print("Registering {}".format(agent))
    batch_size = config.batch_size or len(traces)
    res = register(agent)
    results = [res]
    unvalidated = [skill_name for skill_name, validated in res.items() if not validated]
    print("Training {}".format(agent))
    while traces and unvalidated:
        print(sorted(unvalidated))
        res = train(agent, config | DictTree(batch=traces[:batch_size]))
        traces = traces[batch_size:]
        results.append(res)
        unvalidated = [skill_name for skill_name, validated in res.items() if not validated]
    print('FAILURE :(' if unvalidated else 'SUCCESS :)', sorted(unvalidated))
    return results
