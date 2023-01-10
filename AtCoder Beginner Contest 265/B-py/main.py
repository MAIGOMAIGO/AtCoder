N,M,T = map(int,input().split())
A = list(map(int,input().split()))
XY = [0,0]
if M > 0:
  m = 1
  XY = list(map(int,input().split()))
for i in range(N-1):
  T -= A[i]
  if T <= 0:
    print("No")
    exit(0)
  if i+2 == XY[0]:
    T += XY[1]
    if m < M:
      XY = list(map(int,input().split()))
      m += 1
print("Yes")
