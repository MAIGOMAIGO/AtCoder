N,X = map(int,input().split())
S = list(map(int,input().split()))
c = 0
for i in S:
  if i <= X:
    c += i
print(c)
