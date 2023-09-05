N = int(input())
S = input()
s = 'b'
for i in range(N):
  if S == s:
    print(i)
    exit(0)
  if i%3 == 0:
    s = 'a' + s + 'c'
  elif i%3 == 1:
    s = 'c' + s + 'a'
  elif i%3 == 2:
    s = 'b' + s + 'b'
if S == s:
  print(N)
else:
  print(-1)
