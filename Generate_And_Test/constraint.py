from typing import Set, Dict, Callable, FrozenSet


Constraint = Callable[[Dict[str, any]], bool]

class ConstraintFunction:
    def __init__(self, func: Constraint, vars_involved: Set[str]):
        self.func = func
        self.vars = vars_involved

    def __call__(self, assignment: Dict[str, any]) -> bool:
        return self.func(assignment)