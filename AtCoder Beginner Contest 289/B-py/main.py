N,M = map(int,input().split())
a = list(map(int,input().split()))
rL = [0 for i in range(N+1)]
for i in a:
  rL[i] = 1
L = []
c = 1
for i in range(1,N+1):
  if rL[i] == 1:
    c += 1
  else:
    r = [k+1 for k in range(i-c,i)]
    L += r[::-1]
    c = 1
print(*L)
