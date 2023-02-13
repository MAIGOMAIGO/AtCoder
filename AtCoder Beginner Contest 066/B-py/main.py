import sys
S = input()
if len(S)%2 == 1:
  S = S[:-1]
else:
  S = S[:-2]
while S[:len(S)//2] != S[len(S)//2:]:
  S = S[:-2]
print(len(S))
