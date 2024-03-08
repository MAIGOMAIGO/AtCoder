N,M = map(int,input().split())
A = list(map(int,input().split()))
D = {i+1:0 for i in range(N)}
max_value = 0
min_key = 1
for i in A:
  D[i] += 1
  if max_value == D[i]:
    min_key = min(min_key, i)
  elif max_value < D[i]:
    max_value = D[i]
    min_key = i
  print(min_key)
