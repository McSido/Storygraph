import pprint

import creator
import decoder
import encoder
import graph
import player
from VarStore import VarStore
from story import Story


def check_graph(story):
    print('Cycles:', graph.has_cycles(story))

    print('Shortest path:', graph.find_shortest_end_simple(story))

    print('Dead-ends: ', graph.find_dead_ends(story))


def check_player(story):
    player.cli_player(story)


def check_creator(story):
    creator.main()


def playground(story: Story):
    encoded = encoder.encode_story(story)

    with open('test.json', 'w') as f:
        f.write(encoded)

    decoded = decoder.decode_story(encoded, story.store())

    player.cli_player(decoded)


def main():
    story = creator.create_test_story()

    # check_creator(story)
    # check_graph(story)
    # check_player(story)

    playground(story)


if __name__ == '__main__':
    main()
