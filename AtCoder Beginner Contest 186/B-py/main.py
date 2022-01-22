import numpy as np
H,W = map(int,input().split())
A = np.full((H,W),0).tolist()
for i in range(H):
  A[i] = list(map(int,input().split()))
X = [a - np.amin(A) for a in A]
print(np.sum(X))
