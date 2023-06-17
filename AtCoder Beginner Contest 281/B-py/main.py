def isint(s):
  try:
    int(s, 10)
  except ValueError:
    return False
  else:
    return True

S = input()
if not isint(S[0]) and not isint(S[-1]) and isint(S[1:-1]):
  if 100000 <= int(S[1:-1]) <= 999999 and len(S[1:-1]) == 6:
    print("Yes")
    exit(0)
print("No")
