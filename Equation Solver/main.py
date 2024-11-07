from EQNSOLVER import Solver
from sympy import Equality, symbols, Eq, solve, xfield


x, y, z = symbols('x y z')

Equations = [
    Eq(x**2 + x + 15, 0),
    Eq(5*x**2 + 3*x - 3, 0),
    Eq(3*x**4 - 2*x**2, 5),
    Eq(x * 2*x * 3*x * 4*x, -1),
    Eq(6*x**6 + 5*x**5 + 4*x**4 + 3*x**3 + 2*x**2 + x, 0),
    Eq(3*x + y/(z*x), 0)
]


Solver(Equations, 'x')