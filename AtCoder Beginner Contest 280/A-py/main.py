H,W = map(int,input().split())
S = ""
for i in range(H):
  S += input()
print(S.count('#'))
