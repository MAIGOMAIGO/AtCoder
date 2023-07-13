T = int(input())
for i in range(T):
  N = int(input())
  test = list(map(int,input().split()))
  c = 0
  for j in test:
    if j%2 == 1:
      c += 1
  print(c)
