#!/usr/bin/env python
import numpy as np
np.set_printoptions(linewidth=100)

wvs = [(2,3),(1,2),(3,6),(2,1),(1,3),(5,85)]
n = len(wvs)
W = sum([wv[0] for wv in wvs])
dp = np.zeros((n+1,W+1))

for i in range(1,n+1):
    for w in range(W+1):
        if(w-wvs[i-1][0]>=0):
            dp[i][w] = max(dp[i][w],dp[i-1][w-wvs[i-1][0]]+wvs[i-1][1])
        dp[i][w]  = max(dp[i][w],dp[i-1][w])

print(dp)

# calculation of the combination of items
MAX_WEIGHT=4
ans = max([d[MAX_WEIGHT] for d in dp])
dp2 = dp[:,:MAX_WEIGHT+1]
m, n = np.shape(dp2)
last = dp2[m-1,n-1]
taken = [0]*(m-1)
j = n-1
i = m-1
#print(dp2)
while j > 0 and i > 0:
    i -= 1
    cur = dp2[i,j]

    if last-cur > 0:
        taken[i] = 1
        j = j - wvs[i][0]
        last = dp2[i][j] 
        continue

print("given weight:",MAX_WEIGHT)
print("combination:",taken)
print("maximum value:",ans)
