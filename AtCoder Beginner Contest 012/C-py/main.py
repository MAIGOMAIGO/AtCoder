N = int(input())
D = {}
for i in range(1,10):
  for j in range(1,10):
    if i*j in D:
      D[i*j] += [i,j]
    else:
      D[i*j] = [i,j]
s = 2025 - N
L = D[s]
for i in range(len(L)//2):
  print(L[2*i],'x',L[2*i+1])
