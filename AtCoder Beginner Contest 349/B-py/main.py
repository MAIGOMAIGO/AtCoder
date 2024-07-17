S = input()
s = set(S)
D = dict()
for i in s:
  c = S.count(i)
  if c in D:
    D[c] += 1
  else:
    D[c] = 1
for i in D.keys():
  if D[i] != 0 and D[i] != 2:
    print("No")
    exit(0)
print("Yes")