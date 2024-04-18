N = int(input())
for i in range(N):
  A = list(map(int,input().split()))
  L = [j+1 for j in range(N) if A[j] == 1]
  print(*L)
