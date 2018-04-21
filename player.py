from Node import Node
import pickle
import creator
import pprint


def print_description(current):
    print(f'<<<{current.title}>>>\n')
    print(current.text + '\n')
    for i, nextNode in enumerate(current.get_possible_outgoing()):
        print(f'[{i}] {nextNode[1]}')


def cli_player(game):
    current: Node = game.beginning()
    while True:
        current.update_state()
        print_description(current)
        if game.is_ending(current):
            return  # Maybe ask: restart/exit/...
        choice = input('>> ')

        if not choice:
            choice = 0

        if choice == 'exit':
            return

        if choice == 'vars':
            pprint.pprint(current.store.variables)
            continue

        try:
            current = current.take_outgoing(
                current.get_possible_outgoing()[int(choice)][0])
        except Exception:
            print('ERROR: unknown command')
            continue


def load_story(path: str = 'story.sgf'):  # StoryGraphFile
    # with open(path, 'rb') as story_file:
    #    return pickle.load(story_file)

    return creator.create_test_story()


def main():
    cli_player(load_story())


if __name__ == '__main__':
    main()
