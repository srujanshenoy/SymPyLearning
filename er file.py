from sympy import symbols, Eq, solve

# Define the variable x
x, y = symbols('x y')

# Define the equation
# Equation = Eq((x**2 + x)**2 - 8*(x**2 + x) + 12, 0)
Equation = Eq(x**2 + 8*x - 15, 0)
Equationb = Eq(x**2 + x -1, 0)
f_x = 2*x**2 + 5*x -75 

# Solve for x
solutions = solve(Equationb, x)

# roota, rootb 

print(solutions)

# for i in [5, -15/2]: print(f_x.subs(x, i))