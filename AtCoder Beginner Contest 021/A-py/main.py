N = int(input())
n = [8,4,2,1]
L = []
while N > 0:
  for i in n:
    if N >= i:
      L.append(i)
      N -= i
      break
print(len(L))
for i in L:
  print(i)
