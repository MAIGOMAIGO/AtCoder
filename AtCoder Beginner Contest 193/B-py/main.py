N = int(input())
lo = -1
for i in range(N):
  APX = list(map(int, input().split()))
  if APX[2]-APX[0] > 0:
    if(lo == -1) or (APX[1]<lo):
      lo = APX[1]
print(lo)
