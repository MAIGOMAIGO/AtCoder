A,B = map(int,input().split())
xa,ya = (A-1)%3,(A-1)//3
xb,yb = (B-1)%3,(B-1)//3
if ya==yb and xb-xa==1:
  print("Yes")
else:
  print("No")
