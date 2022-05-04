N = int(input())
S,T = [],[]
for i in range(N):
  st = list(map(str,input().split()))
  S.append(st[0])
  T.append(int(st[1]))
t = sorted(T,reverse=True)
print(S[T.index(t[1])])
