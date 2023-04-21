N,K = map(int,input().split())
c = K
for i in range(N-1):
  c *= K-1
print(c)
