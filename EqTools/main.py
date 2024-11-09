from eqtools import *
from sympy.abc import x, y, z



expressions = [
    x**2 + 2*x + 34,
    x**3 + 12*x**2 + 3*x + 5,
    x**4 + 1,
    (x**2 + 8*x + 15) ** 2,
    x ** 4 + 8*x**2 + 15,
]

mass_factor_expressions(expressions, x)