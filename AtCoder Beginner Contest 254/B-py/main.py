N = int(input())
L = []
for i in range(N):
  L.append(1)
  if i > 1:
    cL = L.copy()
    for j in range(i-1):
      L[j+1] += cL[j]
  print(" ".join([str(s) for s in L]))
