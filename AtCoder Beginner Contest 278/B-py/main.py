H,M = map(int,input().split())
L = []
for i in range(24):
  for j in range(59):
    L.append([i,j])
while True:
  h = "{:02d}".format(H)
  m = "{:02d}".format(M)
  if [int(h[0]+m[0]),int(h[1]+m[1])] in L:
    print(H,M)
    break
  M += 1
  if M >= 60:
    M = 0
    H += 1
    if H >= 24:
      H = 0
