N = int(input())
A = list(map(int,input().split()))
h = 0
for i in A:
  if i < 0:
    if h+i < 0:
      h=0
    else:
      h += i
  else:
    h += i
print(h)
