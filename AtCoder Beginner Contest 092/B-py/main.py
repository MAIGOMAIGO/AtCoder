N = int(input())
D,X = map(int,input().split())
c = X
for i in range(N):
  A = int(input())
  for j in range(D):
    if j * A + 1 > D:
      break
    else:
      c += 1
print(c)
