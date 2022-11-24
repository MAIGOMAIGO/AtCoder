N,M,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(M):
  if A[i] > X:
    print(min(len(A[:i]),len(A[i:])))
    break
