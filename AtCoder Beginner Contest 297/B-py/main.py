S = input()
if S.find("B")%2 == S.rfind("B")%2:
  print("No")
elif S.find("R") < S.find("K") < S.rfind("R"):
  print("Yes")
else:
  print("No")
