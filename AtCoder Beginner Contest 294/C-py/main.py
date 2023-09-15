N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A+B
C.sort()
D = {C[i]:i+1 for i in range(len(C))}
a,b = [],[]
for i in A:
  a.append(D[i])
print(*a)
for i in B:
  b.append(D[i])
print(*b)
