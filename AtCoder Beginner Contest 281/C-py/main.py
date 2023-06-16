N,T = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
p = T%s
for i in range(N):
  if p > A[i]:
    p -= A[i]
  else:
    print(i+1,p)
    break
