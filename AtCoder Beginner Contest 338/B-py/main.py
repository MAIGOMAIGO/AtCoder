S = input()
D = dict()
for i in range(len(S)):
  if S[i] in D:
    D[S[i]] -= 1
  else:
    D[S[i]] = -1
d = sorted(D.items(), key=lambda x: (x[1],x[0]))
print(d[0][0])
