import heapq
def p(a,b):
  if a > b:
    print(a)
  else:
    print(b)
N = int(input())
A = []
B = []
for i in range(N):
  AB = list(map(int,input().split()))
  A.append(AB[0])
  B.append(AB[1])
if A.index(min(A)) != B.index(min(B)):
  p(min(A),min(B))
else:
  a = heapq.nlargest(2,A)
  b = heapq.nlargest(2,B)
  if (min(A) + min(B)) < a[1] and (min(A) + min(B)) < b[1]:
    print(min(A) + min(B))
  elif (min(A) + min(B)) > a[1] or (min(A) + min(B)) > b[1]:
    if a[1] < b[1]:
      p(a[1],min(B))
    else:
      p(min(A),b[1])
