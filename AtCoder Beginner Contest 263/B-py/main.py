N = int(input())
P = list(map(int,input().split()))
c = 1
now = P[-1]
for i in range(N):
  if now == 1:
    break
  now = P[now-2]
  c+=1
print(c)
