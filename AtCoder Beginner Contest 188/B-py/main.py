N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
X = 0
for i in range(N):
  X += (A[i]*B[i])
if(X == 0):
  print("Yes")
else:
  print("No")
