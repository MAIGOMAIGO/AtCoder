N = int(input())
S = input()
m = 0
for i in range(1,N):
  s1 = list(set(S[:i]))
  s2 = list(set(S[i:]))
  c = 0
  for j in s1:
    if j in s2:
      c += 1
  if c > m:
    m = c
print(m)
