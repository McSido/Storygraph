from typing import Union


class VarCommand:
    def __init__(self, variable: str, operator: str,
                 value: Union[str, int]) -> None:
        self.variable = variable
        self.operator = operator
        self.value = value
