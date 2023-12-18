N,M = map(int,input().split())
L = [list(map(int,input().split())) for i in range(N)]
for i in L:
  for j in L:
    if j[0] >= i[0]:
      F = i[2:]
      f = False
      for k in j[2:]:
        if k in F:
          F.remove(k)
        else:
          f = True
          break
      if not f:
        if len(F) > 0 or j[0] > i[0]:
          print("Yes")
          exit(0)
print("No")
