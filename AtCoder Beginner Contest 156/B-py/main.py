N,K = map(int,input().split())
c = 1
while int(N/K):
  N = int(N/K)
  c+=1
print(c)
