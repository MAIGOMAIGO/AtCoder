N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N - 1):
  if A[i] > A[i+1]:
    for j in range(A[i],A[i+1],-1):
      L.append(j)
  else:
    for j in range(A[i],A[i+1]):
      L.append(j)
L.append(A[-1])
print(*L)
