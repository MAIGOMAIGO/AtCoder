N = int(input())
a,b = 0,0
for i in range(N):
  X,Y = map(int,input().split())
  a += X
  b += Y
print("Takahashi" if a > b else "Draw" if a == b else "Aoki")
