N,T = map(int,input().split())
c = 1001
for i in range(N):
  ci,ti = map(int,input().split())
  if T>=ti and ci < c:
    c = ci
print(c) if c <= 1000 else print("TLE")
