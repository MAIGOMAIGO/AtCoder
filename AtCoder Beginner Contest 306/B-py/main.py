A = list(map(int,input().split()))
c = 0
for i,a in enumerate(A):
  c += a*(2**i)
print(c)
