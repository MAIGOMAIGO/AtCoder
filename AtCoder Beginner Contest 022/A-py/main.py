N,S,T = map(int,input().split())
W = int(input())
c = 1 if S <= W <= T else 0
for i in range(N-1):
  A = int(input())
  W += A
  c += 1 if S <= W <= T else 0
print(c)
