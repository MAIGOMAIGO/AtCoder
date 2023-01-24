N = int(input())
a = list(map(int,input().split()))
D = {}
for i in a:
  for j in range(3):
    if j+i-1 in D:
      D[j+i-1] += 1
    else:
      D[j+i-1] = 1
print(max(D.values()))
