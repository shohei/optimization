from pulp import *
import pdb

prob = LpProblem(name='sample',sense=LpMaximize)
x1 = LpVariable('x1',lowBound=0.0)
x2 = LpVariable('x2',lowBound=0.0)
prob += 2*x1 + 3*x2
prob += x1 + 3*x2 <=9, 'ineq1'
prob += x1 + x2 <= 4, 'ineq2'
prob += 2*x1 + x2 <= 6, 'ineq3'
prob.solve()
print(LpStatus[prob.status])
print('optimal value',value(prob.objective))
pdb.set_trace()
for v in prob.variables():
    print(v.name,'=',value(v))



