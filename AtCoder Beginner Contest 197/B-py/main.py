H,W,Y,X = map(int,input().split())
S=[]
for i in range(H):
  S.append(input())
look = 0
for i in reversed(range(0,Y-1)):
  if S[i][X-1] == '#':
    break;
  look+=1
for i in reversed(range(0,X-1)):
  if S[Y-1][i] == '#':
    break;
  look+=1
for i in range(Y,H):
  if S[i][X-1] == '#':
    break;
  look+=1
for i in range(X,W):
  if S[Y-1][i] == '#':
    break;
  look+=1
print(look+1)
