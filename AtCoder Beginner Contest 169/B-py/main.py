import sys
N = int(input())
A = list(map(int,input().split()))
A.sort()
X = 1
max = 10**18
for i in range(N):
  X *= A[i]
  if max < X:
    print(-1)
    sys.exit()
print(X)
