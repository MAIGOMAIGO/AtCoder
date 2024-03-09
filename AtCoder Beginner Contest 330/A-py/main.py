N,L = map(int,input().split())
A = list(map(int,input().split()))
c = 0
for i in A:
  if i >= L:
    c += 1
print(c)
