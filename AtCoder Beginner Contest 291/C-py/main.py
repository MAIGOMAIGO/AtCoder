N = int(input())
S = input()
P = set()
x,y = 0,0
P.add((x,y))
for i in S:
  if i == 'R':
    x += 1
  elif i == 'L':
    x -= 1
  elif i == 'U':
    y += 1
  elif i == 'D':
    y -= 1
  
  if (x,y) in P:
    print("Yes")
    exit(0)
  else:
    P.add((x,y))
print("No")
