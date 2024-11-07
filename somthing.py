############################################################

print("---------------------------------------------------------")

f_x = (x**2 + x)**2 - 8*(x**2 + x) + 12

for root in solutions:
    print(f_x.subs(x, root))

###########################################################

print("--------------------------------------------------------")

from sympy import TableForm
h = [None, ';|;'.join(['e', 's', 'solve(e, s)', 'solve(e, s, dict=True)', 'solve(e, s, set=True)']).split(';')]
t = []
for e, s in [
         (x - y, y),
         (x - y, [x, y]),
         (x**2 - y, [x, y]),
         ([x - 3, y -1], [x, y]),
         ]:
     how = [{}, dict(dict=True), dict(set=True)]
     res = [solve(e, s, **f) for f in how]
     t.append([e, '|', s, '|'] + [res[0], '|', res[1], '|', res[2]])

print(TableForm(t, headings=h, alignments="<"))
