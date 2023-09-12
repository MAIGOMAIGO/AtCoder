N = int(input())
A = set()
c = 0
for i in range(N):
  a = int(input())
  if a in A:
    c += 1
  else:
    A.add(a)
print(c)
