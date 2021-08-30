import numpy as np
import picos as pic
import matplotlib.pyplot as plt

socp=pic.Problem()
H=[0,1,2,3,4,5,6,7]
p=[[44,47],[64,67],[67,9],[83,21],[36,87],[70,88],
   [88,12],[58,65]]
w = [1,2,2,1,2,5,4,1]

X=socp.add_variable('X',2)
d = [socp.add_variable('d['+str(i)+']',1) for i in H]
objective=sum(w[i]*d[i] for i in H)
socp.set_objective('min',objective)
socp.add_list_of_constraints([abs(p[i]-X) < d[i] for i in H])
res = socp.solve(solver='cvxopt')

print(X.value[0])
print(X.value[1])

x=np.array(p)[:,0]
y=np.array(p)[:,1]
plt.scatter(x,y,color='k',marker='+')
plt.scatter(X.value[0], X.value[1], marker='o')
plt.show()



