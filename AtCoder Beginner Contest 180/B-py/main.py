import numpy as np
N = int(input())
X = list(map(int,input().split()))
X = np.abs(X)
print(sum(X))
print(sum([x*x for x in X])**0.5)
print(max(X))
