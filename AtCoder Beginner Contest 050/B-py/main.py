N = int(input())
T = list(map(int,input().split()))
M = int(input())
for i in range(M):
  P,X = map(int,input().split())
  L = T[:P-1] + T[P:]
  print(sum(L)+X)
