N = int(input())
c,a = dict(),dict()
for i in range(N):
  C = int(input())
  A = set(list(map(int,input().split())))
  c[i+1] = C
  a[i+1] = A
X = int(input())
M = []
for i in range(N):
  if X in a[i+1]:
    M.append(i+1)
m = [c[i] for i in M]
x = []
for i in range(len(M)):
  if m[i] == min(m):
    x.append(M[i])
print(len(x))
print(*x)
