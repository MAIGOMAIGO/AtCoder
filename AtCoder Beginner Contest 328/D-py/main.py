S = input()
L = []
for c in S:
  if c == 'C' and (len(L) > 1):
    if (L[-1] == 'B') and (L[-2] == 'A'):
      L.pop()
      L.pop()
      continue
  L.append(c)
print("".join(L))
