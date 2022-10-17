def yaku(N):
  c = 1
  for i in range(1,N):
    if N%i == 0:
      c += 1
  return c

N = int(input())
n = 0
for i in range(1,N+1,2):
  if yaku(i) == 8:
    n += 1
print(n)
