S = input()
T = input()
a = ["AB","BA","BC","CB","CD","DC","DE","ED","AE","EA"]
b = ["AC","CA","AD","DA","BD","DB","BE","EB","CE","EC"]
if S in a and T in a or S in b and T in b or S == T or S[::-1] == T:
  print("Yes")
else:
  print("No")
