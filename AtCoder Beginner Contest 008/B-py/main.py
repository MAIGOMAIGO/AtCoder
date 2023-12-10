N = int(input())
D = {}
for i in range(N):
  S = input()
  if S in D:
    D[S] += 1
  else:
    D[S] = 1
print(max(D,key=D.get))
