N = int(input())
x,y = [],[]
for i in range(N):
  a,b = map(int,input().split())
  x.append(a)
  y.append(b)
t = 0
for i in range(N-1):
  for k in range(i+1,N):
    if t < (x[i]-x[k])**2 + (y[i]-y[k])**2:
      t = (x[i]-x[k])**2 + (y[i]-y[k])**2
print(t**0.5)
