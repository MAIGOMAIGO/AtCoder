A = []
for i in range(9):
  A.append(list(map(int,input().split())))
for i in range(9):
  if len(set(A[i])) != 9:
    print("No")
    exit(0)
for i in range(9):
  L = [A[j][i] for j in range(9)]
  if len(set(L)) != 9:
    print("No")
    exit(0)
for i in range(9):
  x,y = i%3,i//3
  L = [A[3*y+(j//3)][3*x+(j%3)] for j in range(9)]
  if len(set(L)) != 9:
    print("No")
    exit(0)
print("Yes")
