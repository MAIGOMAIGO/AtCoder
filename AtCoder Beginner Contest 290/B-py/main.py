N,K = map(int,input().split())
S = input()
s = ""
c = 0
for i in S:
  if i == 'o' and c < K:
    s += 'o'
    c += 1
  else:
    s += 'x'
print(s)
