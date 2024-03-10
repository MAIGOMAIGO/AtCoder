N,L,R = map(int,input().split())
A = list(map(int,input().split()))
a = []
for i in A:
  if i <= L:
    a.append(str(L))
  elif i >= R:
    a.append(str(R))
  else:
    a.append(str(i))
print(" ".join(a))
