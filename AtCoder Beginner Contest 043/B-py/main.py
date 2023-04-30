s = input()
S = ""
for i in range(len(s)):
  if s[i] == 'B':
    S = S[:-1]
  else:
    S += s[i]
print(S)
