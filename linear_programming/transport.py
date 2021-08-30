from pulp import *
import numpy as np
import pdb

prob = LpProblem("transport", sense=LpMinimize)
x1 = LpVariable('x1',lowBound=0.0)
x2 = LpVariable('x2',lowBound=0.0)
x3 = LpVariable('x3',lowBound=0.0)
y1 = LpVariable('y1',lowBound=0.0)
y2 = LpVariable('y2',lowBound=0.0)
y3 = LpVariable('y3',lowBound=0.0)
prob += x1 + 2*x2 + 3*x3 + 4*y1 + 8*y2 + 7*y3
prob += x1+x2+x3 <= 20
prob += x1+x2+x3 >= 20
prob += y1+y2+y3 <= 15 
prob += y1+y2+y3 >= 15 
prob += x1+y1 <= 8.5 
prob += x1+y1 >= 8.5 
prob += x2+y2 <= 12.5 
prob += x2+y2 >= 12.5 
prob += x3+y3 <= 14 
prob += x3+y3 >= 14 
prob.solve()

print("optimal",value(prob.objective))
for v in prob.variables():
    print(v.name,":",v.varValue)

