N = int(input())
n = 1
m = "1"
while(n ** 3 <= N):
  t = n ** 3
  if str(t) == str(t)[::-1]:
    m = str(t)
  n += 1
print(m)
