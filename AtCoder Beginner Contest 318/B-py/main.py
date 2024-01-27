N = int(input())
S = set()
for i in range(N):
  A,B,C,D = map(int,input().split())
  for x in range(A,B):
    for y in range(C,D):
      S.add((x,y))
print(len(S))
