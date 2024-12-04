 
from GNT import generate_and_test
import constraint

def main():
    def c1(assignment):
        return assignment['var1'] < assignment['var2']

    def c2(assignment):
        return assignment['var2'] != assignment['var3']

    constraint1 = constraint.ConstraintFunction(c1, {'var1', 'var2'})
    constraint2 = constraint.ConstraintFunction(c2, {'var2', 'var3'})

    Vs = {'var1', 'var2', 'var3'}

    Cs = {constraint1, constraint2}

    domains = {
        'var1': {1, 2, 3},
        'var2': {1, 2, 3},
        'var3': {1, 2, 3}
    }

    context = {}

    solutions = generate_and_test(Vs, Cs, context, domains)

    solutions_dict = [dict(sol) for sol in solutions]

    print("Solutions:")
    for sol in sorted(solutions_dict, key=lambda x: (x['var1'], x['var2'], x['var3'])):
        print(sol)

if __name__ == "__main__":
    main()
