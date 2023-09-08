import copy
H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
c = 0
def f(pos,P):
  global c
  if pos[0] == H-1 and pos[1] == W-1:
    c += 1
  
  if pos[1] + 1 < W:
    if A[pos[0]][pos[1]+1] not in P:
      p = copy.deepcopy(P)
      p.add(A[pos[0]][pos[1]+1])
      f([pos[0],pos[1]+1],p)
  
  if pos[0] + 1 < H:
    if A[pos[0]+1][pos[1]] not in P:
      p = copy.deepcopy(P)
      p.add(A[pos[0]+1][pos[1]])
      f([pos[0]+1,pos[1]],p)
  
f([0,0],set([A[0][0]]))
print(c)
