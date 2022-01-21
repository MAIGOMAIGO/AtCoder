def S(s):
  i=0
  for a in range(3):
    i += int(s[a])
  return i
A,B = map(int,input().split())
A = S(str(A))
B = S(str(B))
print(B if A < B else A)
