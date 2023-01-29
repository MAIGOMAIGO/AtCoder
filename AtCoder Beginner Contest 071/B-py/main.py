S = set(input())
s = set("abcdefghijklmnopqrstuvwxyz")
for i in S:
  s.discard(i)
L = sorted(list(s))
print(L[0]) if len(L) > 0 else print(None)
