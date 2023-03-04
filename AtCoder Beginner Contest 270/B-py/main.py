X,Y,Z = map(int,input().split())
if (X > 0 and 0 < Y < X) or (X < 0 and 0 > Y > X):
  if (X > 0 and 0 < Y < Z) or (X < 0 and 0 > Y > Z):
    print(-1)
  else:
    if X > 0 and Z > 0:
      print(X)
    elif X > 0 and Z < 0:
      print(X-2*Z)
    elif X < 0 and Z > 0:
      print(2*Z-X)
    elif X < 0 and Z < 0:
      print(-X)
else:
  print(abs(X))
