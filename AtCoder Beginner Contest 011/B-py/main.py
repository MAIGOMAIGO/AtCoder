S = input()
if len(S) > 1:
  print(S[0].upper() + S[1:].lower())
else:
  print(S[0].upper())
