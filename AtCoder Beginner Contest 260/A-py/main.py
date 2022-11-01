S = input()
if len(set(S)) == 3:
  print(S[0])
elif len(set(S)) == 2:
  if S[0] == S[1]:
    print(S[2])
  elif S[0] == S[2]:
    print(S[1])
  else:
    print(S[0])
else:
  print(-1)
