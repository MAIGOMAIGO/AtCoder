H,W = map(int,input().split())
S,x,y = [],[],[]
for i in range(H):
  S.append(input())
  if 'o' in S[i]:
    y.append(i)
    x.append(S[i].find('o'))
if len(x) < 2:
  y.append(y[0])
  x.append(S[y[0]].rfind('o'))
print(abs(x[1]-x[0])+abs(y[1]-y[0]))
