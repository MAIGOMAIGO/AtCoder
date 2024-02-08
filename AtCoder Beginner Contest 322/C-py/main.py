N,M = map(int,input().split())
A = list(map(int,input().split()))
j,p = 0,0
L = [0 for i in range(N)]
for i in range(N):
  if A[M-p-1] == N-i:
    j = 0
    if M>p+1:
      p+=1
  L[i] = j
  j+=1
for i in L[::-1]:
  print(i)
