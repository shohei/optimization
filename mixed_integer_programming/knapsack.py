from pulp import *

#w = [4,2,2,1,10]
#v = [12,2,1,1,4]
#W = 15
w = [4,2,2,1,10]
v = [12,2,1,1,4]
W = 15
r = range(len(w))

m = LpProblem(sense=LpMaximize)
x = [LpVariable('x%d'%i, cat=LpBinary) for i in r]

m += lpDot(v,x)
m += lpDot(w,x) <= W 
m.solve() 

print('max value: {} / combination:{}'.format(
    value(m.objective),
    [i for i in r if value(x[i])>0.5]))




