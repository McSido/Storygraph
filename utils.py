from collections import namedtuple

VarCommand = namedtuple('VarCommand', ['variable', 'operator', 'value'])


class Game:
    def __init__(self, beginning):
        self._beginning = beginning

    def beginning(self):
        return self._beginning
