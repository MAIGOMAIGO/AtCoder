K,S = map(int,input().split())
c = 0
for X in range(K+1 if K <= S else S+1):
  for Y in range(K+1 if K <= S-X else S-X+1):
    if S-X-Y <= K:
      c += 1
print(c)
