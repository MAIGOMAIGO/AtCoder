H,W = map(int,input().split())
s = set()
G = []
x,y = 1,1
for i in range(H):
  G.append(input())
while True:
  s.add((y,x))
  
  if G[y-1][x-1] == 'U':
    if y > 1:
      y -= 1
    else:
      print(y,x)
      break
  elif G[y-1][x-1] == 'D':
    if y < H:
      y += 1
    else:
      print(y,x)
      break
  elif G[y-1][x-1] == 'L':
    if x > 1:
      x -= 1
    else:
      print(y,x)
      break
  elif G[y-1][x-1] == 'R':
    if x < W:
      x += 1
    else:
      print(y,x)
      break
  
  if (y,x) in s:
    print(-1)
    break
