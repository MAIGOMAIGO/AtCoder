N = int(input())
pt,px,py = 0,0,0
for i in range(N):
  t,x,y = map(int,input().split())
  dt = t - pt
  dx = abs(x - px)
  dy = abs(y - py)
  if dt < dx+dy or (dt-(dx+dy))%2 == 1:
    print("No")
    exit(0)
  else:
    pt,px,py = t,x,y
print("Yes")