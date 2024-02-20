N = int(input())
W = []
X = []
for i in range(N):
  WX = list(map(int,input().split()))
  W.append(WX[0])
  X.append(WX[1])
T = [0] * 24
for i in range(24):
  for j in range(N):
    n = (X[j] + i) % 24
    if 9 <= n < 18:
      T[i] += W[j]
print(max(T))
