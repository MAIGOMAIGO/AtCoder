N = int(input())
L = []
for i in range(1,N+1):
  x = 1
  while True:
    if i%(2**x) != 0:
      break
    x += 1
  L.append(x)
print(L.index(max(L))+1)
