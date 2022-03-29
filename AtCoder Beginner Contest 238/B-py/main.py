N = int(input())
A = list(map(int,input().split()))
r = 0
X = [0]
for a in A:
  r = (r+a)%360
  X.append(r)
X.sort()
X.append(360)
a = []
for i in range(len(X)-1):
  a.append(X[i+1]-X[i])
print(max(a))
