H,W = map(int,input().split())
S = []
L = "snuke"
for i in range(H):
  s = input()
  for j in range(W-5+1):
    if s[j:j+5] == L:
      for k in range(j,j+5):
        print(i+1,k+1)
      exit(0)
    if s[j:j+5] == L[::-1]:
      for k in range(j+5,j,-1):
        print(i+1,k)
      exit(0)
  S.append(s)
for i in range(H-5+1):
  for j in range(W-5+1):
    s = S[i][j]+S[i+1][j+1]+S[i+2][j+2]+S[i+3][j+3]+S[i+4][j+4]
    if s == L:
      for k in range(5):
        print(i+k+1,j+k+1)
      exit(0)
    if s == L[::-1]:
      for k in range(5,0,-1):
        print(i+k,j+k)
      exit(0)
for i in range(H-5+1):
  for j in range(W):
    s = S[i][j]+S[i+1][j]+S[i+2][j]+S[i+3][j]+S[i+4][j]
    if s == L:
      for k in range(5):
        print(i+k+1,j+1)
      exit(0)
    if s == L[::-1]:
      for k in range(5,0,-1):
        print(i+k,j+1)
      exit(0)
for i in range(H-5+1):
  for j in range(4,4+W-5+1):
    s = S[i][j]+S[i+1][j-1]+S[i+2][j-2]+S[i+3][j-3]+S[i+4][j-4]
    if s == L:
      for k in range(5):
        print(i+k+1,j-k+1)
      exit(0)
    if s == L[::-1]:
      for k in range(5,0,-1):
        print(i+k,j-k+2)
      exit(0)
