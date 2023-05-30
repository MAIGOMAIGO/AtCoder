N,Q = map(int,input().split())
a = [0]*N
for i in range(Q):
  L,R,T = map(int,input().split())
  a = [T if L-1 <= i <= R-1 else a[i] for i in range(N)] 
for i in a:
  print(i)
