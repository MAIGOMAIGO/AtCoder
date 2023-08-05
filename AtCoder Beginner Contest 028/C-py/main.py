ABCDE = list(map(int,input().split()))
L = []
for i in range(3):
  for j in range(i+1,4):
    for k in range(j+1,5):
      L.append(ABCDE[i] + ABCDE[j] + ABCDE[k])
L.sort(reverse=True)
print(L[2])
