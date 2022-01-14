N,K = map(int,input().split())
i = 0
for n in range(N):
  for k in range(K):
    i += ((n+1)*100 + k+1)
print(i)
