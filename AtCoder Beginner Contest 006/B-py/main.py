n = int(input())
L = [0,0,1]
if n > 3:
  for i in range(3,n):
    L.append((L[i-3]+L[i-2]+L[i-1])%10007)
  print(L[-1])
else:
  print(L[n-1])
