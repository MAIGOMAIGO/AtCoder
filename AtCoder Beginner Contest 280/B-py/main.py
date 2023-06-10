N = int(input())
S = list(map(int,input().split()))
L = []
for i in range(N):
  L.append(S[i]-sum(L))
print(*L)
