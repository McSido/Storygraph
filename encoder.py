import json
from typing import Any, Dict, List, Tuple, Union

from Node import Node
from story import Story
from utils import VarCommand
from VarStore import VarStore


def encode_var_store(store: VarStore) -> str:

    return json.dumps(store.variables)


def encode_story(story: Story)-> str:
    story_dict: Dict[str, Any] = {}

    story_dict['beginning'] = story.beginning().__hash__()
    story_dict['endings'] = [n.__hash__() for n in story._endings]

    nodes = {}
    for node in story._nodes:
        nodes[node.__hash__()] = _encode_node(node)

    story_dict['nodes'] = nodes

    return json.dumps(story_dict)


def _encode_node(node: Node) -> Dict[str, Union[str, List[Any]]]:
    node_dict: Dict[str, Union[str, List[Any]]] = {}

    node_dict['title'] = node.title
    node_dict['text'] = node.text
    # Outgoing
    node_dict['requirements'] = [
        _encode_var_command(c) for c in node.requirements]
    node_dict['changes'] = [
        _encode_var_command(c) for c in node.changes]
    node_dict['outgoing'] = _encode_outgoing(node.outgoing)

    return node_dict


def _encode_outgoing(out: Dict[Node, Tuple[str, List[VarCommand]]]):
    ret = {}
    for node, info in out.items():
        ret[node.__hash__()] = {info[0]: [_encode_var_command(c)
                                          for c in node.changes]}
    return ret


def _encode_var_command(command: VarCommand):
    return command.__dict__
