N = int(input())
S = ""
L = []
for i in range(1,10):
  if N%i == 0:
    L.append(i)
for i in range(N+1):
  n = -1
  for j in L:
    if i%(N/j) == 0:
      n = j
      break
  if n < 0:
    S += "-"
  else:
    S += str(n)
print(S)
