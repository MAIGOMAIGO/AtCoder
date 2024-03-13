N = int(input())
A = list(map(int,input().split()))
L = sorted(A)
M = sum(A)
D = dict()
for i in range(N-1):
  M -= L[i]
  if L[i] not in D:
    if L[i+1] != L[i]:
      D[L[i]] = M
D[L[-1]] = 0
X = [D[i] for i in A]
print(*X)
