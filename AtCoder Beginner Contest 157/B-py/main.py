A = [list(map(int,input().split())) for i in range(3)]
N = int(input())
for i in range(N):
  b = int(input())
  for j in range(3):
    if b in A[j]:
      A[j][A[j].index(b)] = -1
for i in range(3):
  if A[i].count(-1) == 3:
    print("Yes")
    exit()
  x = [a[i] for a in A]
  if x.count(-1) == 3:
    print("Yes")
    exit()
if A[0][0]==A[1][1]==A[2][2]==-1 or A[0][2]==A[1][1]==A[2][0]==-1:
  print("Yes")
  exit()
print("No")
