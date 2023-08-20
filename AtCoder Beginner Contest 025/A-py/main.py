S = list(input())
N = int(input())
L = []
for i in S:
  for j in S:
    L.append(i+j)
L.sort()
print(L[N-1])
