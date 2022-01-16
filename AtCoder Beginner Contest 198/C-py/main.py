R,X,Y=map(int,input().split())
Z=(X**2+Y**2)**0.5
if Z==R:
  print(1)
elif Z<=2*R:
  print(2)
else:
  if Z%R == 0:
    print(int(Z/R))
  else:
    print(int(Z/R)+1)
