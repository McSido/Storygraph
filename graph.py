from story import Story
from Node import Node
from typing import Set
import math


def has_cycles(story: Story) -> bool:

    def find_cycle(node: Node, seen: Set[Node]) -> bool:
        i_seen = set(seen)
        if node in i_seen:
            return True

        i_seen.add(node)
        for next in node.outgoing:
            if find_cycle(next, i_seen):
                return True
        return False

    return find_cycle(story.beginning(), set())


def find_shortest_end_simple(story: Story)-> float:
    if not story.has_ending():
        return math.inf

    def inner_shortest_end_simple(node: Node, seen: Set[Node],
                                  story: Story) -> float:
        i_seen = set(seen)
        if node in i_seen:
            # Cycle: quit
            return math.inf
        if story.is_ending(node):
            return 0

        if not node.outgoing:
            return math.inf

        i_seen.add(node)
        return min(inner_shortest_end_simple(n, i_seen, story)
                   for n in node.outgoing) + 1

    return inner_shortest_end_simple(story.beginning(), set(), story)


def find_dead_ends(story: Story) -> Set[Node]:

    dead_ends: Set[Node] = set()

    def inner_dead_ends(node: Node, seen: Set[Node],
                        story: Story, dead_ends: Set[Node]):
        i_seen = set(seen)
        if node in i_seen:
            # Cycle: quit
            return

        i_seen.add(node)

        if not node.outgoing and not story.is_ending(node):
            dead_ends.add(node)
            return

        for next in node.outgoing:
            inner_dead_ends(next, i_seen, story, dead_ends)

    inner_dead_ends(story.beginning(), set(), story, dead_ends)

    return dead_ends
