N = int(input())
L = [2,1]
for i in range(2,N+1):
  L.append(L[i-2] + L[i-1])
print(L[-1])
