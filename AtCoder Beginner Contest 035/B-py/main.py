S = input()
T = int(input())
x,y,c = 0,0,0
for i in range(len(S)):
  if S[i] == 'L':
    x -= 1
  elif S[i] == 'R':
    x += 1
  elif S[i] == 'U':
    y += 1
  elif S[i] == 'D':
    y -= 1
  elif S[i] == '?':
    c += 1
d = abs(x)+abs(y)
if T == 1:
  print(d+c)
else:
  print((c-d)%2) if d <= c else print(d-c)
