N = int(input())
a = list(map(int,input().split()))
if sum(a)%N == 0:
  ave = sum(a)//N
  s,c = 0,0
  for i in range(N):
    if a[i] > ave:
      s += a[i] - ave
    elif a[i] < ave:
      s -= ave - a[i]
    if s != 0:
      c += 1
  print(c)
else:
  print(-1)
