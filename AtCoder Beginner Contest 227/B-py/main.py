L = []
for a in range(1,1001):
    for b in range(1,1001):
      L.append(4*a*b+3*a+3*b)
N = int(input())
S = list(map(int,input().split()))
c = 0
for i in S:
  if i in L:
    c+=1
print(N-c)
