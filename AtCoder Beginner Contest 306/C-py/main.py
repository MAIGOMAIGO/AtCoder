N = int(input())
A = list(map(int,input().split()))
D = {i:0 for i in range(1,N+1)}
L = []
for i in range(1,3*N+1):
  D[A[i-1]] += 1
  if D[A[i-1]] == 2:
    L.append(A[i-1])
print(*L)
