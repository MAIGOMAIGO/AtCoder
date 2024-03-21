import sys
sys.setrecursionlimit(20000000)

N = int(input())
tree = {i:set() for i in range(1,N+1)}
for i in range(N-1):
  v1,v2 = map(int,input().split())
  tree[v1].add(v2)
  tree[v2].add(v1)
old = [False]*N
p = [0]*N

def f(point, pare):
  old[point-1] = True
  if len(tree[point]) == 0:
    p[point-1] += 1
  else:
    a = 0
    for i in tree[point]:
      a += f(i, point) if pare != i else 0
    p[point-1] = a + 1
  return p[point-1]

if len(tree[1]) == 1:
  print(1)
  exit(0)

C = [0] * len(tree[1])
old[0] = True
c = 0
for i in tree[1]:
  C[c] = f(i, 1)
  c += 1
print(sum(C)-max(C) + 1)
