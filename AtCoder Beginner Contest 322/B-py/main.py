N,M = map(int,input().split())
S = input()
T = input()
if T.find(S) == 0 and T.rfind(S) == M-N:
  print(0)
elif T.find(S) == 0:
  print(1)
elif T.rfind(S) == M-N:
  print(2)
else:
  print(3)
