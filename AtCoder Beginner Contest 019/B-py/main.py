s = input()
S,c = s[0],1
for i in range(1,len(s)):
  if S[-1] == s[i]:
    c += 1
  else:
    S += str(c) + s[i]
    c = 1
print(S + str(c))
