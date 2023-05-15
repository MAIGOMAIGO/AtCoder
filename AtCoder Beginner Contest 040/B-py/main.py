n = int(input())
L = []
for y in range(1,n+1):
  x = n//y
  s = x*y
  L.append(n-s + abs(x-y))
print(min(L))
