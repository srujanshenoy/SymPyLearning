from sympy import symbols, Eq, solve, simplify, sqrt

a, b, c = symbols("a b c")
x = symbols("x")
 
print((c/a)**1/3 / (1/a))


# Quadratic_1 = Eq(a*x**2 + b*x + c, 0)
# Quadratic_2 = Eq(c*x**2 + b*x + a, 0)

# a = 12
# b = 4
# c = 5

# print(solve(Quadratic_1, x))
# print(solve(Quadratic_2, x))

Complicated_aplha_beta_eq = Eq((-b + sqrt(b**2 - 4*a*c)) / 2*a, ((-b + sqrt(b**2 - 4*a*c)) / 2*a) ** 2)

simplified_alpha_beta_eq = simplify(Complicated_aplha_beta_eq)

print(simplified_alpha_beta_eq)

## Eq(a*(-b + sqrt(-4*a*c + b**2))/2, a**2*(b - sqrt(-4*a*c + b**2))**2/4)

## Get the eqn to have rhs of 0

newsimplifiedalphabetaeqn = simplify(Eq(simplified_alpha_beta_eq.lhs - simplified_alpha_beta_eq.rhs, 0))