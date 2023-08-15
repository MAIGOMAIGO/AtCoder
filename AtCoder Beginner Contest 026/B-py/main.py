import math
N = int(input())
R = []
for i in range(N):
  R.append(int(input()))
R.sort(reverse=True)
if N > 1:
  S = R[0]*R[0] - R[1]*R[1]
  for i in range(2,N):
    if i%2 == 0:
      if i == N-1:
        S += R[i]*R[i]
      else:
        S += R[i]*R[i] - R[i+1]*R[i+1]
  print(S*math.pi)
else:
  print(R[0]*R[0]*math.pi)
