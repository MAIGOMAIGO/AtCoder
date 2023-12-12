N = int(input())
A = []
for i in range(N):
  A.append(input())
L = A[0]
for i in range(1,N-1):
  L += A[i][N-1]
L += A[N-1][::-1]
for i in range(N-2,0,-1):
  L += A[i][0]
L = L[-1] + L[:-1]

A[0] = L[:N]
for i in range(1,N-1):
  A[i] = A[i][:N-1] + L[N+i-1]
S = L[N+N-2:N+N-2+N]
A[N-1] = S[::-1]
for i in range(N-2,0,-1):
  A[i] = L[-i] + A[i][1:]
for i in A:
  print(i)
