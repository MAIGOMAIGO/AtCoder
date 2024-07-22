N = int(input())
A = 0
B = 0
for i in range(N):
  a,b = map(int,input().split())
  A += a
  B = max(B, b-a)
print(A+B)