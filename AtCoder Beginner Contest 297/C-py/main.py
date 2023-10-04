H,W = map(int,input().split())
c = 0
for i in range(H):
  S = input()
  for j in range(W-1):
    if S[j]=="T" and S[j+1]=="T":
      S = S[:j] + "PC" + S[j+2:]
  print(S)
