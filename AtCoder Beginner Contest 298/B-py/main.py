N = int(input())
A,B = [],[]
for i in range(N):
  A.append(list(map(int,input().split())))
for i in range(N):
  B.append(list(map(int,input().split())))
for i in range(4):
  A = list(map(list,zip(*A[::-1])))
  f = True
  for j in range(N):
    for k in range(N):
      if A[j][k] != B[j][k] and A[j][k] == 1:
      	f = False
      	break
  if f:
    print("Yes")
    exit(0)
print("No")
