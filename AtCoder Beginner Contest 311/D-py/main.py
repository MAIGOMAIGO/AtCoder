import sys
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
S = [input() for i in range(N)]
c = 0
P = set()
p = set()

def f(pos,dur):
  global p,P,S
  dx,dy = 0,0
  if dur == 0: # ↑
    dy = -1
  elif dur == 1: # →
    dx = 1
  elif dur == 2: # ↓
    dy = 1
  elif dur == 3: # ←
    dx = -1
  x,y = pos[0],pos[1]
  while(True):
    p.add((x,y))
    if S[y+dy][x+dx] == "#":
      if (x,y) not in P:
        P.add((x,y))
        for i in range(4):
          f((x,y),i)
      break
    else:
      x += dx
      y += dy
for i in range(4):
  f((1,1),i)
print(len(p))
