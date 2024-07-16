N = int(input())
D = dict()
for i in range(N):
  A,C = map(int, input().split())
  if C in D:
    D[C] = min(D[C],A)
  else:
    D[C] = A
print(max(D.values()))