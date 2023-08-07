N,K = map(int,input().split())
S = []
for i in range(N):
  S.append(input())
s = S[:K]
s.sort()
for i in s:
  print(i)
