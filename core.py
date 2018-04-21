import creator
import graph
import player


def check_graph(story):
    print('Cycles:', graph.has_cycles(story))

    print('Shortest path:', graph.find_shortest_end_simple(story))

    print('Dead-ends: ', graph.find_dead_ends(story))


def check_player(story):
    player.cli_player(story)


def check_creator():
    pass


def main():
    story = creator.create_test_story()
    check_graph(story)


if __name__ == '__main__':
    main()
