N,A,B = map(int,input().split())
p = 0
for i in range(N):
  s,d = map(str,input().split())
  if int(d) < A:
    d = A
  elif int(d) > B:
    d = B
  else:
    d = int(d)
  if s == 'East':
    p += d
  elif s == 'West':
    p -= d
if p == 0:
  print(0)
elif p > 0:
  print("East",p)
elif p < 0:
  print("West",-p)
