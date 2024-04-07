H,W,N = map(int,input().split())
L = ["."*W for i in range(H)]
x,y,v = 0,0,0
for i in range(N):
  pv = 0
  if L[y][x] == ".":
    L[y] = L[y][:x] + "#" + L[y][x+1:]
    pv += 1
  else:
    L[y] = L[y][:x] + "." + L[y][x+1:]
    pv -= 1
  v = (v + pv) % 4
  if v < 0:
    v = 3
  if v == 0:
    y -= 1
  elif v == 1:
    x += 1
  elif v == 2:
    y += 1
  elif v == 3:
    x -= 1
  
  if x < 0:
    x = W-1
  if y < 0:
    y = H-1
  if x >= W:
    x = 0
  if y >= H:
    y = 0
for i in range(H):
  print(L[i])
