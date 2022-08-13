N,K = map(int,input().split())
A = list(map(int,input().split()))
X,Y = [],[]
for i in range(N):
  XY = list(map(int,input().split()))
  X.append(XY[0])
  Y.append(XY[1])
R = []
for i in range(N):
  if not i+1 in A:
      a = []
      for j in A:
        a.append((X[j-1]-X[i])**2+(Y[j-1]-Y[i])**2)
      R.append(min(a))
print(max(R)**0.5)
