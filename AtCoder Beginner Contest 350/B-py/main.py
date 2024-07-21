N,Q = map(int,input().split())
T = list(map(int,input().split()))
L = [True for i in range(N)]
for i in T:
  L[i-1] = not L[i-1]
print(L.count(True))