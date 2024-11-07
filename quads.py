from sympy import Eq, symbols, solve, TableForm

x = symbols('x')


Equations = [
    Eq(x**2 + x - 1, 0),
    Eq(x**2 - 5*x + 6, 0),
    Eq(2*x**2 + 3*x - 2, 0),
    Eq(x**2 - 4, 0)
]


data = []
# Prepare the data
for equation in Equations:
    solution = solve(equation, x)
    data.append([equation, *solution])  # Unpack the solution list

# Find the maximum number of solutions any equation has
max_solutions = max(len(solve(eq, x)) for eq in Equations)

# Create headings as two parts
headings = ['Equation', 'Solutions']

# Adjust the data rows to match the number of solutions columns
for row in data:
    # Add empty values for missing solutions
    row.extend([None] * (max_solutions - len(row)))

# Now print the table
print(TableForm(data, headings=headings))

