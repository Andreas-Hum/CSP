from typing import Set, Dict, Callable, FrozenSet

import constraint


def generate_and_test(
    Vs: Set[str],
    Cs: Set[constraint.ConstraintFunction],
    context: Dict[str, any],
    domains: Dict[str, Set[any]],
) -> Set[FrozenSet]:
    cs = [c for c in Cs if c.vars.issubset(context.keys())]

    for constraint in cs:
        if not constraint(context):
            return set()

    if not Vs:
        return {frozenset(context.items())}

    var = next(iter(Vs))
    remaining_vars = Vs - {var}
    sols = set()
    for val in domains[var]:
        new_context = context.copy()
        new_context[var] = val

        new_solutions = generate_and_test(remaining_vars, Cs, new_context, domains)
        sols.update(new_solutions)

    return sols
