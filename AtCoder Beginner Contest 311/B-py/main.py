N,D = map(int,input().split())
S = input()
for i in range(N-1):
  s = input()
  for j in range(D):
    if S[j] == "o" and s[j] == "x":
      S = S[:j] + "x" + S[j+1:]
L = S.split("x")
c = [len(i) for i in L]
print(max(c))
