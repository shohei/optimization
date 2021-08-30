import numpy as np
from cvxopt import solvers, matrix

Q = matrix(np.array([[2.0, -1.0],[-1.0,3.0]]))
c=matrix(np.array([-2.0,-4.0]))
A=matrix(np.array([[-1.0,0.0],[0.0,-1.0],[2.0,3.0],[1.0,4.0]]))
b=matrix(np.array([0.0,0.0,6.0,5.0]))

sol = solvers.qp(P=Q,q=c,G=A,h=b)
print(sol)
print(sol["x"])
print(sol["primal objective"])

