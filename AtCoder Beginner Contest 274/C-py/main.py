N = int(input())
A = list(map(int,input().split()))
L = [0] * (2*N+2)
for i in range(1,N+1):
  L[2*i] = L[A[i-1]] + 1
  L[2*i+1] = L[A[i-1]] + 1
for i in L[1:]:
  print(i)
