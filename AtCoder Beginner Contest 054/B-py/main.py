N,M = map(int,input().split())
A,B = [],[]
for i in range(N):
  A.append(input())
for i in range(M):
  B.append(input())
for i in range(N-M+1):
  for j in range(N-M+1):
    if A[i][j] == B[0][0]:
      f = True
      for y in range(M):
        for x in range(M):
          if A[i+y][j+x] != B[y][x]:
            f = False
            break
      if f:
        print("Yes")
        exit(0)
print("No")
