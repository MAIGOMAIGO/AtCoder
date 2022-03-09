N,D = map(int,input().split())
c = 0
for i in range(N):
  X,Y = map(int,input().split())
  if D*D >= X*X + Y*Y:
    c+=1
print(c)
