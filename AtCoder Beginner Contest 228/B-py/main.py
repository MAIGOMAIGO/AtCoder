N,X = map(int,input().split())
A = list(map(int,input().split()))
c = 1
a = A[X-1]
A[X-1] = 0
for i in range(N):
  if A[a-1] != 0:
    b = a
    a = A[b-1]
    A[b-1] = 0
    c+=1
  else:
    break
print(c)
