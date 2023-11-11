N,M,H,K = map(int,input().split())
S = input()
item = set()
for i in range(M):
  x,y = map(int,input().split())
  item.add((x,y))
p = [0,0]
for i in range(N):
  if S[i] == "R":
    p[0] += 1
  elif S[i] == "L":
    p[0] -= 1
  elif S[i] == "U":
    p[1] += 1
  elif S[i] == "D":
    p[1] -= 1
  H -= 1
  if H < 0:
    print("No")
    exit(0)
  if H < K:
    if (p[0],p[1]) in item:
      item.remove((p[0],p[1]))
      H = K
print("Yes")
