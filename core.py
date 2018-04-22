import creator
import graph
import player


def check_graph(story):
    print('Cycles:', graph.has_cycles(story))

    print('Shortest path:', graph.find_shortest_end_simple(story))

    print('Dead-ends: ', graph.find_dead_ends(story))


def check_player(story):
    player.cli_player(story)


def check_creator(story):
    creator.main()


def main():
    story = creator.create_test_story()
    # creator.save_story(story)

    # check_creator(story)
    check_graph(story)
    check_player(story)


if __name__ == '__main__':
    main()
