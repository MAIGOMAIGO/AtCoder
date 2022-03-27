import sys
N = int(input())
A = 1
while 3**A < N:
  B = 1
  while 3**A+5**B < N:
    B += 1
  if 3**A+5**B == N:
    print(A,B)
    sys.exit()
  else:
    A += 1
print(-1)
