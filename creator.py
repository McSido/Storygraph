from Node import Node
from VarStore import VarStore
from utils import VarCommand
from pprint import pprint
from story import Story
import pickle


def create_test_story() -> Story:

    store = VarStore()
    story = Story()

    # Create nodes
    n1 = story.create_node('n1', store)
    n2 = story.create_node('n2', store)
    n3 = story.create_node('n3', store)
    n4 = story.create_node('n4', store)
    end1 = story.create_node('end1', store)
    dead1 = story.create_node('dead-end', store)

    n1.set_text('Currently at n1')
    n2.set_text('Currently at n2')
    n3.set_text('Currently at n3')
    n4.set_text('Currently at n4')
    end1.set_text('Ending #1')
    dead1.set_text('Dead-end reached')

    block3 = VarCommand('test', '=', 5)
    goto_4_1 = [VarCommand('test', '+', 7), VarCommand('test2', '+', 'abd')]
    req4 = VarCommand('test', '=', 5)

    n3.add_change(block3)
    n4.add_requirement(req4)

    n1.add_outgoing(n2, 'Goto 2', None)
    n1.add_outgoing(n3, 'Goto 3', None)
    n2.add_outgoing(n3, 'Goto 3', None)
    n3.add_outgoing(n4, 'Goto 4', None)
    n3.add_outgoing(dead1, 'Goto dead-end', None)
    n4.add_outgoing(end1, 'Goto ending 1', None)
    n4.add_outgoing(n1, 'Goto 1', goto_4_1)

    story.change_beginning(n1)
    story.add_ending(end1)

    return story


def save_story(story: Story, path: str = 'story.sgf'):
    with open(path, 'wb') as file:
        return pickle.dump(story, file)
