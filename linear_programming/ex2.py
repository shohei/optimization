from pulp import *
import numpy as np
import pdb

A = np.array([[3,1,2],[1,3,0],[0,2,4]])
c = np.array([150,200,300])
b = np.array([60,36,48])
(m,n) = A.shape
prob = LpProblem(name='production',sense=LpMaximize)
x = [LpVariable('x'+str(i+1), lowBound=0) for i in range(n)]
prob += lpDot(c,x) #objective function
for i in range(m):
    prob += lpDot(A[i],x) <= b[i], 'ineq'+str(i)
print(prob)
prob.solve()

X = np.array([v.varValue for v in prob.variables()])
print(X)
print(np.all(np.abs(b - np.dot(A,X)) <= 1.0e-5))


print(LpStatus[prob.status])
print('optimal value=',value(prob.objective))
#pdb.set_trace()
for v in prob.variables():
    #print(v.name,'=',v.varValue)
    print(v.name,'=',value(v))









