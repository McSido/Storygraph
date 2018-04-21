from Node import Node
from VarStore import VarStore


class Story:
    def __init__(self):
        self._beginning = None
        self._nodes = set()
        self._endings = set()

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

    def create_node(self, title: str, store: VarStore) -> Node:
        new_node = Node(title, store)
        if not self._nodes:
            self._beginning = new_node
        self._nodes.add(new_node)
        return new_node
