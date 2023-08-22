S = input()
sl = S.lower()
for i in range(len(S)):
  if S[i] != sl[i]:
    print(i+1)
    break
