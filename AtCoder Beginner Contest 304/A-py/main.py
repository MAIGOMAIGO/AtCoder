N = int(input())
S,A = [],[]
for i in range(N):
  s,a = map(str,input().split())
  A.append(int(a))
  S.append(s)
S = S[A.index(min(A)):] + S[:A.index(min(A))]
for i in S:
  print(i)
