N = int(input())
A = []
for i in range(N):
  A.append(input())
for i in range(N):
  B = input()
  if A[i] != B:
    for j in range(N):
      if A[i][j] != B[j]:
        print(i+1,j+1)
        exit(0)