import numpy as np
import cdd
from itertools import combinations
MEPS = 1.0e-6
import pdb
import time

np.random.seed(2)
n,d = 40, 3
A = np.random.randint(0,100,(n,d))
b = np.sqrt(np.dot(A**2,np.ones(d))).astype(np.int64)
m,n = np.shape(A)

eb = np.hstack((b,np.zeros(n))).reshape(-1,1)
eA = np.vstack((-A,np.identity(n)))
ar = np.hstack((eb,eA))
mat = cdd.Matrix(ar, number_type='fraction')
poly = cdd.Polyhedron(mat)

ext = poly.get_generators()
vl = np.array([np.array(v[1:])/v[0] for v in ext if v[0] != 0])
vlist = vl.astype(np.float64)

#pdb.set_trace()
zerosets = [set([i for i in range(m+n)
                if abs(eb[i]+np.dot(eA[i],v)) <= MEPS]) for v in vl]
elist = [[i,j] for i, j in combinations(range(len(vl)),2)
        if len(zerosets[i].intersection(zerosets[j])) >= 2]


from vpython import *
scene = canvas(width=800, height=600)
vmin = np.min(vlist)-0.5
length = np.max(vlist)-vmin+0.5
scene.up = vector(0,0,1)
scene.forward = vector(-1,-1,-1)
scene.center = vector(0,0,0)
scene.range = 0.9*length
scene.background = color.white
cb = color.black

arrow(pos=vector(vmin,0,0), axis = vector(length,0,0),
        shaftwidth=0.002,headwidth=0.05,color=cb)
arrow(pos=vector(0,vmin,0), axis = vector(0,length,0),
        shaftwidth=0.002,headwidth=0.05,color=cb)
arrow(pos=vector(0,0,vmin), axis = vector(0,0,length),
        shaftwidth=0.002,headwidth=0.05,color=cb)

for v in vlist:
    sphere(pos=vector(*v),radius=0.01,color=cb) 
    time.sleep(0.1)

for [i,j] in elist:
    curve(pos=[vector(*vlist[i]), vector(*vlist[j])], radius=0.007, color=cb) 
    time.sleep(0.1)

