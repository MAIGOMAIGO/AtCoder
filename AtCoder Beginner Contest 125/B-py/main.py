N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
L = []
for i in range(N):
  if V[i]-C[i] > 0:
    L.append(V[i]-C[i])
print(sum(L))
