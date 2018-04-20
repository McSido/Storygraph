from typing import Any, Dict, List, Tuple

from utils import VarCommand
from VarStore import VarStore


class Node(object):
    def __init__(self, title: str, store: VarStore) -> None:
        self.title: str = title
        self.text: str = ""
        self.outgoing: Dict[Node, Tuple[str, List[VarCommand]]] = {}
        self.requirements: List[VarCommand] = []
        self.changes: List[VarCommand] = []
        self.store: VarStore = store

    def set_text(self, text: str):
        self.text = text

    def add_outgoing(self, node: Any, text: str, changes: List[VarCommand]):
        self.outgoing[node] = (text, changes)

    def get_possible_outgoing(self) -> List[Tuple[Any, str]]:
        ret = []
        for out, info in self.outgoing.items():
            if not out.requirements:
                ret.append((out, info[0]))
            elif all(self.store.compare(a) for a in out.requirements):
                ret.append((out, info[0]))

        return ret

    def add_change(self, change: VarCommand):
        self.changes.append(change)

    def take_outgoing(self, node: Any):
        if self.outgoing[node][1]:
            for c in self.outgoing[node][1]:
                self.store.update(c)

        return node

    def add_requirement(self, req: VarCommand):
        self.requirements.append(req)

    def update_state(self):
        for c in self.changes:
            self.store.update(c)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title
