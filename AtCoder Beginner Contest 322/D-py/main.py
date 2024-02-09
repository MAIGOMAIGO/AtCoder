P = [[],[],[]]
for i in range(3):
  for j in range(4):
    p = input()
    for k in range(4):
      if p[k] == "#":
        P[i].append((j,k))
if len(P[0])+len(P[1])+len(P[2]) != 16:
  print("No")
  exit(0)

R = dict()
R[(0,0)]=(0,3);R[(0,1)]=(1,3);R[(0,2)]=(2,3);R[(0,3)]=(3,3);
R[(1,0)]=(0,2);R[(1,1)]=(1,2);R[(1,2)]=(2,2);R[(1,3)]=(3,2);
R[(2,0)]=(0,1);R[(2,1)]=(1,1);R[(2,2)]=(2,1);R[(2,3)]=(3,1);
R[(3,0)]=(0,0);R[(3,1)]=(1,0);R[(3,2)]=(2,0);R[(3,3)]=(3,0);
def rotate(p):
  L = []
  for i in p:
    L.append(R[i])
  return L

def checkMap(x1,y1,x2,y2,x3,y3):
  M = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  x = [x1,x2,x3]
  y = [y1,y2,y3]
  for i in range(3):
    for j in P[i]:
      if 0 <= j[1]+y[i] < 4 and 0 <= j[0]+x[i] < 4:
        M[j[1]+y[i]][j[0]+x[i]] = 1
      else:
        return False
  for i in range(4):
    for j in range(4):
      if M[i][j] == 0:
        return False
  return True

for ix in range(-3,4):
  for iy in range(-3,4):
    for jr in range(4):
      P[1] = rotate(P[1])
      for jx in range(-3,4):
        for jy in range(-3,4):
          for kr in range(4):
            P[2] = rotate(P[2])
            for kx in range(-3,4):
              for ky in range(-3,4):
                if checkMap(ix,iy,jx,jy,kx,ky):
                  print("Yes")
                  exit(0)
print("No")
