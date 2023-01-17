H,W = map(int,input().split())
S = []
for i in range(H):
  S.append(input())
  S[i] = S[i].replace('.','0')
for i in range(H):
  for j in range(W):
    if S[i][j] != '#':
      s = ""
      if i > 0:
        s += S[i-1][j]
      if i > 0 and j > 0:
        s += S[i-1][j-1]
      if j > 0:
        s += S[i][j-1]
      if j > 0 and i < H-1:
        s += S[i+1][j-1]
      if i < H-1:
        s += S[i+1][j]
      if i < H-1 and j < W-1:
        s += S[i+1][j+1]
      if j < W-1:
        s += S[i][j+1]
      if j < W-1 and i > 0:
        s += S[i-1][j+1]
      S[i] = S[i][:j] + str(s.count('#')) + S[i][j+1:]
  print(S[i])
