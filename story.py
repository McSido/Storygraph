from Node import Node
from VarStore import VarStore
from typing import Set, Optional


class Story:
    def __init__(self, store: VarStore)->None:
        self._beginning: Optional[Node] = None
        self._nodes: Set[Node] = set()
        self._endings: Set[Node] = set()
        self._store = store

    def store(self)->VarStore:
        return self._store

    def beginning(self):
        return self._beginning

    def add_ending(self, node: Node):
        self._endings.add(node)

    def remove_ending(self, node: Node):
        self._endings.remove(node)

    def is_ending(self, node: Node)-> bool:
        return node in self._endings

    def has_ending(self) -> bool:
        return bool(self._endings)

    def change_beginning(self, beginning: Node):
        self._beginning = beginning

    def create_node(self, title: str) -> Node:
        new_node = Node(title, self._store)
        if not self._nodes:
            self._beginning = new_node
        self._nodes.add(new_node)
        return new_node
