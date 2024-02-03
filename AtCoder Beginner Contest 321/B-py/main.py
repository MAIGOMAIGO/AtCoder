N,X = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
s = sum(A[1:-1])
if sum(A[:-1]) >= X:
  print(0)
elif sum(A[1:]) < X:
  print(-1)
elif sum(A[1:]) == X:
  print(A[-1])
else:
  print(X-s if 100 >= X-s > 0 else -1 if X-s > 0 else 0)
