N = int(input())
A = [[],[]]
A[0] = list(map(int,input().split()))
A[1] = list(map(int,input().split()))
m = 0
for i in range(N):
  c = sum(A[0][:i+1]) + sum(A[1][i:])
  m = c if c > m else m
print(m)