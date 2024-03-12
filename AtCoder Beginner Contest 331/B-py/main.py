N,S,M,L = map(int,input().split())
s = -(-N//6)
m = -(-N//8)
l = -(-N//12)
e = min(s*S,m*M,l*L)
for i in range(s+1):
  for j in range(m+1):
    for k in range(l+1):
      if i*6 + j*8 + k*12 >= N:
        e = min(e, i*S + j*M + k*L)
print(e)
