n,X = map(int,input().split())
a = list(map(int,input().split()))
L = []
for i in range(n):
  if (X >> i)&1 == 1:
    L.append(a[i])
print(sum(L))
