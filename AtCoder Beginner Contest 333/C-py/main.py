N = int(input())
L = [int("1"*i)for i in range(1,13)]
s = set()
for a in L:
  for b in L:
    for c in L:
      s.add(a+b+c)
X = sorted(s)
print(X[N-1])
