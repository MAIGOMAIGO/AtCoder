N = int(input())
A = list(map(int,input().split()))
X = set([i+1 for i in range(N)])
for i in range(N):
  if i+1 in X:
    X.discard(A[i])
print(len(X))
print(*X)
