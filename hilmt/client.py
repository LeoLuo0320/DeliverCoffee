import json

import requests as req

from utils import DictTree

SERVER_URL = 'http://localhost:5000'


def delete(agent):
    return DictTree(req.delete('{}/agent/{}/{}/'.format(SERVER_URL, agent.domain_name, agent.task_name)).json())


def register(agent):
    print("Debug Starts: ")
    for skill, skill_class in agent.get_skill_set().items():
        print("Key is ", skill, ". Type is ", type(skill))
        print("Value is ", skill_class, ". Type is ", type(skill_class))
    data = json.dumps(agent.get_skill_set(), cls=DictTree.JSONEncoder)
    print("\nData is ", data)
    return DictTree(req.post('{}/agent/{}/{}/'.format(SERVER_URL, agent.domain_name, agent.task_name), data=data).json())


def train(agent, config):
    data = json.dumps(config, cls=DictTree.JSONEncoder)
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
