N,K = map(int,input().split())
A = list(map(str,input().split()))
for i in range(K):
  A = A[1:] + ['0']
print(" ".join(A))
