N = int(input())
P = list(map(int,input().split()))
if N > 1:
  print(max(P[1:])-P[0]+1 if max(P[1:])-P[0] >= 0 else 0)
else:
  print(0)
