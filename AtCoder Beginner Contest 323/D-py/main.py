N = int(input())
D = dict()
for i in range(N):
  S,C = map(int,input().split())
  while(C > 0):
    if S in D:
        C += D[S]
    if C > 1: # 複数
      D[S] = C%2
      C = C//2
      S *= 2
    else:# 1匹
      D[S] = C
      C = 0
print(sum(D.values()))
