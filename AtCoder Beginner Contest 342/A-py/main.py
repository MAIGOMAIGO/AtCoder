S = input()
c = S[0]
if S.count(c) == 1:
  print(1)
else:
  for i in range(len(S)):
    if c != S[i]:
      print(i+1)
