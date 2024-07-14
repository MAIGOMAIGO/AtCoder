N,K = map(int,input().split())
A = set(list(map(int,input().split())))
m = ((K+1)*K)//2
for i in A:
  m -= 0 if i > K else i
print(m)