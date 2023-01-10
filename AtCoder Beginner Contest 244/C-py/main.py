N = int(input())
L = [i+1 for i in range(2*N+1)]
for i in range(N+1):
  print(L[0])
  L = L[1:]
  n = int(input())
  if n != 0:
    L.remove(n)
