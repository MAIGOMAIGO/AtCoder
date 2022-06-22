N,A,B = map(int,input().split())
w,b,f = ".","#",True
S,s = "",""
for i in range(N):
  S += w*B if f else b*B
  s += b*B if f else w*B
  f = not f
f = True
for i in range(1,N*A+1):
  print(S) if f else print(s)
  if i%A == 0:
    f = not f
