N = int(input())
T = input()
x = y = r = 0
for i in range(N):
  if T[i] == "S":
    if r == 0:
      x+=1
    elif r == 1:
      y-=1
    elif r == 2:
      x-=1
    else:
      y+=1
  else:
    r = (r+1)%4
print(x,y)
