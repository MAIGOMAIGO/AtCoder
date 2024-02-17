N = int(input())
S = [i for i in input()]
S.sort()
rS = sorted(S,reverse=True)
low = int("".join(S))
high = int("".join(rS))
c = 0
for i in range(int(low**0.5),int(high**0.5)+2):
  n = str(i**2)
  if len(n) < N:
    n += "0"*(N-len(n))
  elif len(n) > N:
    break
  if sorted(n) == S:
    c += 1
print(c)
