S = input()
s = 0
for i in range(len(S)):
  if s == 0:
    if S[i] != "A":
      s = 1
  elif s == 1:
    if S[i] == "C":
      s = 2
    elif S[i] == "A":
      print("No")
      exit(0)
  elif s == 2:
    if S[i] != "C":
      print("No")
      exit(0)
print("Yes")
