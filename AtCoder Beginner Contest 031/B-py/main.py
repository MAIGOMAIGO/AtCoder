L,H = map(int,input().split())
N = int(input())
for i in range(N):
  A = int(input())
  print(L-A) if L>=A else print(0) if H>=A else print(-1)
