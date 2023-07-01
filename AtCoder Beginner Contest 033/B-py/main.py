N = int(input())
S,P = [],[]
for i in range(N):
  SP = list(map(str,input().split()))
  S.append(SP[0])
  P.append(int(SP[1]))
m = max(P)
s = sum(P)
if m/s > 0.5:
  print(S[P.index(m)])
else:
  print("atcoder")
