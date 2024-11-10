from sympy import Eq, Equality, solve, symbols

class ExpressionProcessor:
    def __init__(self, expressions):

        from sympy import symbols

        self.x, self.y, self.z, self.a ,self.b, self.c, self.alpha, self.beta, self.gamma, self.d = symbols(r'x y z a b c \alpha \beta \gamma d')


        # Check if all elements are valid SymPy expressions
        if all(self.is_valid_expression(expr) for expr in expressions):
            self.expressions = expressions
        else:
            raise TypeError("All elements must be valid SymPy expressions.")

    def print_expression(self, index, _print=True):
        # Format the expression for better readability
        inputstring = str(self.expressions[index])
        
        # Compatibility for removing prefix/suffix in older Python versions
        if inputstring.startswith("Eq(") and inputstring.endswith(")"):
            inputstring = inputstring[3:-1]
        
        # Display using caret (^) notation
        inputstring = inputstring.replace("**", "^")
        
        if _print:
            print(inputstring)
        
        return inputstring

    @staticmethod
    def is_valid_expression(expr):
        # Verify that the input is a valid SymPy expression
        return hasattr(expr, 'free_symbols')

    def is_multinomial(self, expr):
        # Check if the expression is a polynomial in all its variables
        return expr.is_polynomial(*expr.free_symbols)

    def is_multinomial_list(self):
        # Validate that all expressions are multinomials
        return all(self.is_multinomial(expr) for expr in self.expressions)

    def factor_expressions(self):
        # Factorize each expression if it’s a multinomial
        if self.is_multinomial_list():
            for index, expr in enumerate(self.expressions):
                print("Original:", self.print_expression(index, _print=False))
                print("Factored form:", expr.factor())

class EquationProcessor(ExpressionProcessor):
    def __init__(self, equations):
        # Ensure all items are of type Equality
        if all(isinstance(eq, Equality) for eq in equations):
            super().__init__(equations)
        else:
            raise TypeError("All elements must be of type 'Equality' from SymPy.")

        self.equations = equations

    def print_equation(self, eq, _print=True):
        # Display a formatted version of the equation
        lhs, rhs = eq.lhs, eq.rhs
        print(f"{lhs} = {rhs}") if _print else None
        return f"{lhs} = {rhs}"


    def solve_equations(self, variable):
        # Solve each equation for the specified variable
        solutions = [solve(eq, variable) for eq in self.equations]
        for eq, sol in zip(self.equations, solutions):
            
            print(f"Solutions for {self.print_equation(eq, False)}:")

            for s in sol:
                print(f"  {variable} = {s}")
            print()


# Usage example
# x = symbols('x')
# expressions = [
#     x**2 + x + 15,
#     5*x**2 + 3*x - 3
# ]

# equations = [
#     Eq(x**2 + x + 15, 0),
#     Eq(5*x**2 + 3*x - 3, 0)
# ]

# expr_processor = ExpressionProcessor(expressions)
# expr_processor.factor_expressions()

# equation_processor = EquationProcessor(equations)
# equation_processor.solve_equations(x)
