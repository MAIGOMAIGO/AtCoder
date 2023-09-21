N = int(input())
A = list(map(int,input().split()))
D = dict()
for i in A:
  if i not in D:
    D[i] = 1
  else:
    D[i] += 1
c = 0
for i in D.values():
  c += i//2
print(c)
