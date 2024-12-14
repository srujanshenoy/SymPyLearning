# Import necessary modules from SymPy
from sympy import Eq, Equality, solve, symbols

# Define a class to process mathematical expressions
class ExpressionProcessor:
    """
    A class for processing and manipulating mathematical expressions using SymPy.
    """
    def __init__(self, expressions):
        """
        Initializes the ExpressionProcessor with a list of expressions.
        Defines common symbols used in expressions.
        """
        from sympy import symbols
        # Define common mathematical symbols
        self.x, self.y, self.z, self.a ,self.b, self.c, self.alpha, self.beta, self.gamma, self.d = symbols(r'x y z a b c \alpha \beta \gamma d')


        # Check if all elements are valid SymPy expressions
        if all(self.is_valid_expression(expr) for expr in expressions):
            self.expressions = expressions
        else:
            raise TypeError("All elements must be valid SymPy expressions.")

    def print_expression(self, index, _print=True):
        """
        Formats and prints a SymPy expression in a more readable format.
        
        Args:
            index: The index of the expression in the expressions list.
            _print: A boolean indicating whether to print the expression.
        """
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
        """
        Checks if the given input is a valid SymPy expression.
        
        Args:
            expr: The input to be checked.
        """
        return hasattr(expr, 'free_symbols')

    def is_multinomial(self, expr):
        """
        Checks if the given expression is a multinomial.
        
        Args:
            expr: The expression to be checked.
        """
        return expr.is_polynomial(*expr.free_symbols)

    def is_multinomial_list(self):
        """
        Checks if all expressions in the list are multinomials.
        """
        return all(self.is_multinomial(expr) for expr in self.expressions)

    def factor_expressions(self):
        """
        Factorizes each expression in the list if it's a multinomial.
        """
        if self.is_multinomial_list():
            for index, expr in enumerate(self.expressions):
                print("Original:", self.print_expression(index, _print=False))
                print("Factored form:", expr.factor())

# Define a class to process equations, inheriting from ExpressionProcessor
class EquationProcessor(ExpressionProcessor):
    """
    A class for processing and solving equations, inheriting from ExpressionProcessor.
    """
    def __init__(self, equations):
        # Ensure all items are of type Equality
        if all(isinstance(eq, Equality) for eq in equations):
            super().__init__(equations)
        else:
            raise TypeError("All elements must be of type 'Equality' from SymPy.")

        self.equations = equations

    def print_equation(self, eq, _print=True):
        """
        Prints an equation in a readable format.
        
        Args:
            eq: The equation to be printed.
            _print: A boolean indicating whether to print the equation.
        """
        lhs, rhs = eq.lhs, eq.rhs
        print(f"{lhs} = {rhs}") if _print else None
        return f"{lhs} = {rhs}"


    def solve_equations(self, variable):
        # Solve each equation for the specified variable
        """
        Solves each equation for the specified variable.
        
        Args:
            variable: The variable to solve for.
        """
        solutions = [solve(eq, variable) for eq in self.equations] # get solutions for the equations for the specific variable
        for eq, sol in zip(self.equations, solutions):
            
            print(f"Solutions for {self.print_equation(eq, False)}:")

            for s in sol:
                print(f"  {variable} = {s}")
            print()


# Usage example
#x = symbols('x') # define a symbol 'x'
#expressions = [ # list of expressions
#    x**2 + x + 15, 
#    5*x**2 + 3*x - 3
#]

#equations = [ # list of equations
#    Eq(x**2 + x + 15, 0), # equation 1
#    Eq(5*x**2 + 3*x - 3, 0) # equation 2
#]

#expr_processor = ExpressionProcessor(expressions) # create an instance of ExpressionProcessor
#expr_processor.factor_expressions() # factor the expressions

#equation_processor = EquationProcessor(equations) # create an instance of EquationProcessor
#equation_processor.solve_equations(x) # solve the equations for x
