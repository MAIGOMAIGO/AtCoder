S,T = input(),input()
s = []
for i in range(len(S)):
  if S[i]!=T[i]:
    s.append(i)
if len(s) == 2:
  if S[s[0]]==T[s[1]] and S[s[1]]==T[s[0]]:
  	print("Yes") if s[0]+1 == s[1] else print("No")
  else:
    print("No")
elif len(s)==0:
  print("Yes")
else:
  print("No")
