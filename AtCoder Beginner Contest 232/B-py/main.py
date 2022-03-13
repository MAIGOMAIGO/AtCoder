import sys
S = input()
T = input()
g = ord(S[0]) - ord(T[0])
for i in range(len(S)):
  if ord(S[i]) - ord(T[i]) != g:
    if ord(S[i]) - g - 26 != ord(T[i]) and ord(S[i]) - g + 26 != ord(T[i]):
      print("No")
      sys.exit()
print("Yes")
