N = int(input())
S = [i for i in input()]
Q = int(input())
T = []
l = 0
for i in range(Q):
  t,x,c = map(str,input().split())
  if t == "2":
    l = i
  elif t == "3":
    l = i
  T.append((t,x,c))
for i in range(Q):
  if T[i][0] == "1":
    S[int(T[i][1])-1] = T[i][2]
  else:
    if l == i:
      if T[i][0] == "2":
        S = [s.lower() for s in S]
      elif T[i][0] == "3":
        S = [s.upper() for s in S]
print("".join(S))
