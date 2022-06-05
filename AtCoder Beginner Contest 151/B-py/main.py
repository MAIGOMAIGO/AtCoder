N,K,M = map(int,input().split())
A = list(map(int,input().split()))
if M*N <= sum(A)+K:
  print(N*M-sum(A)) if N*M>sum(A) else print(0)
else:
  print(-1)
