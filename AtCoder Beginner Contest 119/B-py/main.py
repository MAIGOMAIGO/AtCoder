N = int(input())
m = 0
for i in range(N):
  x,u = map(str,input().split())
  if u == "BTC":
    m += float(x)*380000
  else:
    m += int(x)
print(m)
