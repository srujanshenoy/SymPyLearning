from sympy import Equality, symbols, Eq, solve, Symbol

x = symbols('x')

Sample_Equations = [
    Eq(x**2 + x + 15, 0),
    Eq(5*x**2 + 3*x - 3, 0),
    Eq(3*x**4 - 2*x**2, 5),
    Eq(x * 2*x * 3*x * 4*x, -1),
    Eq(6*x**6 + 5*x**5 + 4*x**4 + 3*x**3 + 2*x**2 + x, 0)
]

def is_equality_list(equality_list):
    # Check if all elements in the list are of type Equality
    if all(isinstance(item, Equality) for item in equality_list):
        return True
    else:
        raise TypeError("All elements must be of type 'Equality' from SymPy.")



def is_multinomial(expr):
    # Get all variables (symbols) in the expression
    variables = expr.free_symbols
    
    # Check if the expression is a polynomial in all its variables
    return expr.is_polynomial(*variables)

def is_multinomiallist(exprlist):
    if all(is_multinomial(expr) for expr in exprlist):
        return True
    else:
        raise TypeError("All elements must be multinomials.")




def eqprint(inputstring):
    inputstring = str(inputstring)

    inputstring = inputstring.removesuffix(")") if inputstring.startswith("Eq(") else inputstring 
    inputstring = inputstring.removeprefix("Eq(")
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

def mass_solve_equations(expressions, variable):

    if is_equality_list(expressions):

        solutions = [solve(eq, variable) for eq in expressions]

        for index in range(0, len(expressions)):
            print()
            printeqn(expressions[index])

            for solution in solutions[index]:
                print(f"    x = {solution}")

def mass_factor_expressions(expressions: list, variable):

    if is_multinomiallist(expressions):
        for expression in expressions:
            eqprint(expression)
            eqprint(expression.factor())


        
