N,Q = map(int,input().split())
pos = [(i,0) for i in range(N,0,-1)]
for i in range(Q):
  query = input().split()
  if query[0] == "1":
    C = query[1]
    p = pos[-1]
    if C == "L":
      pos.append((p[0]-1, p[1]))
    elif C == "U":
      pos.append((p[0], p[1]+1))
    elif C == "R":
      pos.append((p[0]+1, p[1]))
    elif C == "D":
      pos.append((p[0], p[1]-1))
  elif query[0] == "2":
    p = pos[-(int(query[1]))]
    print(p[0],p[1])
