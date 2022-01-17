def chan(S,A,B):
  S[A-1],S[B-1] = S[B-1],S[A-1]
  return S
N = int(input())
S = list(input())
Q = int(input())
t = False
for i in range(Q):
  T,A,B = map(int,input().split())
  if T == 1:
    if t:
      if A > N:
        S = chan(S,A-N,B-N)
      elif B <= N:
        S = chan(S,A+N,B+N)
      else:
        S = chan(S,A+N,B-N)
    else:
      S = chan(S,A,B)
  elif T == 2:
    t = not t
if t:
  S[:N],S[N:] = S[N:],S[:N]
print("".join(S))
