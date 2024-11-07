from sympy import symbols, simplify

a, c = symbols('a c')

Expr = ((c/a)**2)**1/3
simplify_expr = c**2/(3*a**2)

a = 3
c = 4

print(Expr.subs(a, c))
print(simplify_expr.subs(a, c))


print(simplify(Expr))