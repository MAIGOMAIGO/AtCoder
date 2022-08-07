N = int(input())
W = list(map(int,input().split()))
g = []
for i in range(1,N):
  S1 = sum(W[:i])
  S2 = sum(W[i:])
  g.append(abs(S2-S1))
print(min(g))
