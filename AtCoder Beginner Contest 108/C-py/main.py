N,K = map(int,input().split())
n = (N//K)**3
if K%2 == 0:
  x = (N + K // 2) // K
  n = n + x**3
print(n)