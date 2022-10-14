H,W = map(int,input().split())
a = []
for i in range(H):
  ai = input()
  if '#' in ai:
    a.append(ai)
for i in range(W):
  f = True
  for j in a:
    if j[i] == '#':
      f = False
      break
  if f:
    a = [j[:i]+' '+j[i+1:] for j in a]
for i in a:
  print(i.replace(' ',''))
