from sympy import Equality, symbols, Eq, solve




def is_equality_list(equality_list):
    # Check if all elements in the list are of type Equality
    if all(isinstance(item, Equality) for item in equality_list):
        return True
    else:
        raise TypeError("All elements must be of type 'Equality' from SymPy.")


def eqprint(inputstring):
    inputstring = str(inputstring)

    inputstring = inputstring.removeprefix("Eq(")
    inputstring = inputstring.removesuffix(")")
    inputstring.replace('**', '^')

    print(inputstring)
    return inputstring

def printeqn(Equation: Equality):
    inputstring = f"{Equation.lhs} = {Equation.rhs}"

    inputstring = inputstring.removeprefix("Eq(")
    inputstring = inputstring.removesuffix(")")
    inputstring.replace('**', '^')

    print('  ' + inputstring)
    return inputstring

def Solver(expressions, variable):

    from sympy import Equality, symbols, Eq, solve

    if is_equality_list(expressions):

        solutions = [solve(eq, variable) for eq in expressions]

        for index in range(0, len(expressions)):
            print()
            printeqn(expressions[index])

            for solution in solutions[index]:
                print(f"    x = {solution}")



x = symbols('x')

Equations = [
    Eq(x**2 + x + 15, 0),
    Eq(5*x**2 + 3*x - 3, 0),
    Eq(3*x**4 - 2*x**2, 5),
    Eq(x * 2*x * 3*x * 4*x, -1),
    Eq(6*x**6 + 5*x**5 + 4*x**4 + 3*x**3 + 2*x**2 + x, 0)
]