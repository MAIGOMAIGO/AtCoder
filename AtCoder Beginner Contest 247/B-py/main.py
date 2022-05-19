N = int(input())
s,t = [],[]
for i in range(N):
  st = list(map(str,input().split()))
  s.append(st[0])
  t.append(st[1])
for i in range(N):
  c1,c2 = 0,0
  for j in range(N):
    if i != j:
      if s[i]==s[j] or s[i]==t[j]:
        c1 = 1
      if t[i]==s[j] or t[i]==t[j]:
        c2 = 1
  if c1 == c2 == 1:
    print('No')
    exit()
print('Yes')
