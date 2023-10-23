H,W = map(int,input().split())
C = []
for i in range(H):
  C.append(input())
S = set()
X = [0 for i in range(min(H,W))]
for i in range(H):
  for j in range(W):
    if (i,j) not in S:
      if C[i][j] == '#':
        p = 1
        S.add((i,j))
        while True:
          if i+p < H and j+p < W:
            if C[i+p][j+p] != '#':
              break
          else:
            break
          S.add((i+p,j+p))
          p += 1
        p = p//2
        X[p-1] += 1
        y,x = i+p,j+p
        while p > 0:
          S.add((y+p,x-p))
          S.add((y-p,x+p))
          p -= 1
print(*X)
