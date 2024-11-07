from sympy import symbols, Eq, solve

# Define the variable x
x = symbols('x')

# Define the equation
Equation = Eq((x**2 + x)**2 - 8*(x**2 + x) + 12, 0)

# Solve for x
solutions = solve(Equation, x)
print(solutions)

############################################################

print("---------------------------------------------------------")

f_x = (x**2 + x)**2 - 8*(x**2 + x) + 12
