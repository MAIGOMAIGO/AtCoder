N = int(input())
A = list(map(int,input().split()))
A.sort()
for i in range(N):
  if min(A)+i != A[i]:
    print(min(A)+i)
    exit(0)
