K,G,M = map(int,input().split())
g,m = 0,0
for i in range(K):
  if g == G:
    g = 0
  elif m == 0:
    m = M
  else:
    if m + g > G:
      m = m+g-G
      g = G
    else:
      g += m
      m = 0
print(g,m)
