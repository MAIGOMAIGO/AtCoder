N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def ABC(L,V,eL):
  for i in eL:
    L[i] = -1
  sL = sorted(L,reverse=True)
  tL = []
  for i in range(V):
    tL.append(L.index(sL[i]))
    L[L.index(sL[i])] = -1
  return tL

LA = ABC(A,X,[])
LB = ABC(B,Y,LA)
C = [A[i]+B[i] for i in range(N)]
LAB = LA+LB
LC = ABC(C,Z,LAB)
L = LAB + LC
L.sort()
for i in L:
  print(i+1)
