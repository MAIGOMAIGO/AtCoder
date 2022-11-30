N = int(input())
s = {}
for i in range(N):
  str = input()
  if str not in s:
    s[str] = 1
  else:
    s[str] += 1
M = int(input())
t = {}
for i in range(M):
  str = input()
  if str not in t:
    t[str] = 1
  else:
    t[str] += 1
c = 0
for i in s.items():
  if i[0] in t:
    if i[1] - t[i[0]] > c:
      c = i[1] - t[i[0]]
  else:
    if i[1] > c:
      c = i[1]
print(c)
