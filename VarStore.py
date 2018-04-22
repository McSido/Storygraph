from utils import VarCommand
from typing import Any

# Change to Singleton


class VarStore(object):
    def __init__(self, variables={}):
        self.variables = variables

    def _create(self, change: VarCommand):
        var = change.variable.rstrip()

        if var.endswith('[]'):
            self.variables[var] = []
        else:
            try:
                int(change.value)
                init_val: Any = 0
            except ValueError:
                init_val = ''
            self.variables[var] = init_val

    def update(self, change: VarCommand):
        if change.variable not in self.variables.keys():
            self._create(change)

        var = change.variable.rstrip()

        if change.operator == '=':
            self.variables[var] = change.value
        elif change.operator == '-':
            self.variables[var] = self.variables[var] + change.value
        elif change.operator == '+':
            self.variables[var] = self.variables[var] + change.value

    def compare(self, comp: VarCommand):
        var = comp.variable.rstrip()
        op = comp.operator
        val = comp.value

        if var not in self.variables.keys():
            return False

        if op == '=':
            return self.variables[var] == val
        if op == '<':
            return self.variables[var] < val
        if op == '>':
            return self.variables[var] > val

    def get_var(self, name):
        if name in self.variables.keys():
            return self.variables[name]
        return None
