N = int(input())
for i in range(N+1):
  for j in range(N-i+1):
    for k in range(N-i-j+1):
      print(i, j, k)
