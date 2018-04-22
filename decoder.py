import json
from typing import Any, Dict, List, Tuple, Union

from Node import Node
from story import Story
from utils import VarCommand
from VarStore import VarStore


def decode_var_store(data: str) -> VarStore:
    return VarStore(json.loads(data))


def decode_story(data: str, store: VarStore) -> Story:
    story = Story(store)

    node_store: Dict[str, Node] = {}

    story_dict = json.loads(data)

    for node_hash, node_dict in story_dict['nodes'].items():
        node = _decode_basic_node(node_dict, story)
        node_store[str(node_hash)] = node

    story.change_beginning(node_store[str(story_dict['beginning'])])

    for ending in story_dict['endings']:
        story.add_ending(node_store[str(ending)])

    for node_hash, node_dict in story_dict['nodes'].items():
        _decode_outgoing(node_store[str(node_hash)],
                         node_store, node_dict['outgoing'])

    return story


def _decode_basic_node(node_dict, story: Story) -> Node:
    node = story.create_node(node_dict['title'])
    node.set_text(node_dict['text'])

    for req in node_dict['requirements']:
        node.add_requirement(_decode_var_command(req))
    for change in node_dict['changes']:
        node.add_change(_decode_var_command(change))

    return node


def _decode_var_command(com_dict)->VarCommand:
    command = VarCommand('', '', None)
    command.__dict__ = com_dict

    return command


def _decode_outgoing(node: Node, node_store, outgoing):
    for out_node_hash, info in outgoing.items():
        out_node = node_store[str(out_node_hash)]
        for text, commands_dict in info.items():
            commands = [_decode_var_command(com) for com in commands_dict]

            node.add_outgoing(out_node, text, commands)
