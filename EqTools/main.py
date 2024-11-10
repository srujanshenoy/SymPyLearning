from oop_math_tools import *

# If i define the below ExpressionProcessor object without the line from sympy.abc import x, will it give me an error?
expressions_object = ExpressionProcessor([
    x**2 + 2*x + 34,
    x**3 + 12*x**2 + 3*x + 5,
    x**4 + 1,
    (x**2 + 8*x + 15) ** 2,
    x ** 4 + 8*x**2 + 15,
])

equations_object = EquationProcessor([
    Eq(x**2 + 2*x + 34, 0),
    Eq(x**3 + 12*x**2 + 3*x + 5, 0),
    Eq(x**4 + 1, 0),
    Eq((x**2 + 8*x + 15) ** 2, 0),
    Eq(x ** 4 + 8*x**2 + 15, 0),
])
equations_object.solve_equations(x)