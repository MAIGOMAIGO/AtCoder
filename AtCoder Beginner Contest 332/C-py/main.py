N,M = map(int,input().split())
S = input()
L = S.split('0')
c = 0
for i in L:
  n = len(i)
  logo = i.count('2')
  if c < logo:
    c = logo
  if n > c+M:
    c += n-(c+M)
print(c)
