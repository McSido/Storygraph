from Node import Node
from VarStore import VarStore
from utils import VarCommand
from pprint import pprint
from utils import Game


def create_test_game() -> Game:

    store = VarStore()

    # Create nodes
    n1 = Node('n1', store)
    n2 = Node('n2', store)
    n3 = Node('n3', store)
    n4 = Node('n4', store)

    n1.set_text('Currently at n1')
    n2.set_text('Currently at n2')
    n3.set_text('Currently at n3')
    n4.set_text('Currently at n4')

    block3 = VarCommand('test', '=', 5)
    goto_4_1 = [VarCommand('test', '+', 7), VarCommand('test2', '+', 'abd')]
    req4 = VarCommand('test', '=', 5)

    n3.add_change(block3)
    n4.add_requirement(req4)

    n1.add_outgoing(n2, 'Goto 2', None)
    n2.add_outgoing(n3, 'Goto 3', None)
    n1.add_outgoing(n3, 'Goto 3', None)
    n3.add_outgoing(n4, 'Goto 4', None)
    n4.add_outgoing(n1, 'Goto 1', goto_4_1)

    # Run story

    return Game(n1)
