N = int(input())
S = set()
for i in range(N):
  A = int(input())
  if A in S:
    S.discard(A)
  else:
    S.add(A)
print(len(S))
