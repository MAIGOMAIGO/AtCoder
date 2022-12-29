N = int(input())
A = list(map(int,input().split()))
c = 0
f = True
while f:
  for i in range(N):
    if A[i]%2 == 0:
      A[i] = A[i]/2
    else:
      f = False
      break
  c += 1
print(c-1)
