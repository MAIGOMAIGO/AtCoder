N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
c = 0
for i in B:
  c += A[i-1]
print(c)
