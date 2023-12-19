N = int(input())
S = set()
for i in range(N):
  s = input()
  if s[::-1] not in S:
    S.add(s)
print(len(S))
