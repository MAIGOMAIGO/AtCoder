S = input()
D = dict()
for i in S:
  if i in D:
    D[i] += 1
  else:
    D[i] = 1
if len(D) == 1:
  print(1)
else:
  c = ((len(S)-1)/2)*len(S)
  f = False
  for i in D.keys():
    c -= ((D[i]-1)/2)*D[i]
    if D[i] > 1:
      f = True
  print(int(c)+1 if f else int(c))
