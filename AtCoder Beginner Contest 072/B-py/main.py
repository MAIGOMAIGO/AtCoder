s = input()
S = ""
for i in range(len(s)):
  if i%2 == 0:
    S += s[i]
print(S)
