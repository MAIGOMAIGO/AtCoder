K = int(input())
if K > 9:
  L = [0,1]
  while K > 10:
    L[0] += 1
    for i in range(len(L)-1):
      if L[i] == L[i+1]:
        L[i] = i
        L[i+1] += 1
    if L[-1] == 10:
      l = len(L)
      L[-1] = l-1
      L.append(l)
    K -= 1
  N = 0
  for i in range(len(L)):
    N += L[i]*(10**i)
  print(N)
else:
  print(K)
