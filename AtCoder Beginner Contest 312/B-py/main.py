N,M = map(int,input().split())
S = []
for i in range(N):
  S.append(input())

for i in range(N-9+1):
  for j in range(M-9+1):
    b =  S[i][j:j+3]+S[i+1][j:j+3]+S[i+2][j:j+3]
    b += S[i+6][j+6:j+9]+S[i+7][j+6:j+9]+S[i+8][j+6:j+9]
    w = S[i][j+3]+S[i+1][j+3]+S[i+2][j+3]+S[i+3][j:j+4]
    w += S[i+6][j+5]+S[i+7][j+5]+S[i+8][j+5]+S[i+5][j+5:j+9]
    if '.' not in b and '#' not in w:
      print(i+1,j+1)
