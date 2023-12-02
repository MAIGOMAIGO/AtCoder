HA,WA = map(int,input().split())
A = set()
for i in range(HA):
  a = input()
  for j in range(WA):
    if a[j] == "#":
      A.add((i,j))
HB,WB = map(int,input().split())
B = set()
for i in range(HB):
  b = input()
  for j in range(WB):
    if b[j] == "#":
      B.add((i,j))
HX,WX = map(int,input().split())
X = set()
for i in range(HX):
  x = input()
  for j in range(WX):
    if x[j] == "#":
      X.add((i,j))

#ここからチェック
for ai in range(-HA+1,HX):
  for aj in range(-WA+1,WX):
    for bi in range(-HB+1,HX):
      for bj in range(-WB+1,WX):
        s = set()
        f = True
        for a in A:
          ay,ax = a[0]+ai,a[1]+aj
          if (ay,ax) in X:
            s.add((ay,ax))
          else:
            f = False
            break
        for b in B:
          by,bx = b[0]+bi,b[1]+bj
          if (by,bx) in X:
            s.add((by,bx))
          else:
            f = False
            break
        if f and len(s) == len(X):
          print("Yes")
          exit(0)
print("No")
