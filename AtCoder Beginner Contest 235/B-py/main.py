N = int(input())
H = list(map(int,input().split()))
t = 0
for h in H:
  if t < h:
    t = h
  else:
    break
print(t)
