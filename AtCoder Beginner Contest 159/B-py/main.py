S = input()
if S == S[::-1]:
  S1 = S[:len(S)//2]
  if S1 == S1[::-1]:
    S2 = S[len(S)//2]
    if S2 == S2[::-1]:
      print("Yes")
      exit()
print("No")
