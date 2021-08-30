# coding:utf-8
#pulpでは線形計画問題以外は解けない

from pulp import *

prob = LpProblem("test",sense=LpMinimize)
x1=LpVariable('x1',lowBound=0.0)
x2=LpVariable('x2',lowBound=0.0)

prob+=(x1-10)*(x1-10)+(x2-8)*(x2-8)
prob+= 2*x1 + 3*x2 <= 18
prob.solve()
print(value(prob.objective))
for v in prob.variables():
    print(v.name,":",v.varValue)

