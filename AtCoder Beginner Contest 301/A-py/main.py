N = int(input())
S = input()
if S.count("T") > S.count("A"):
  print("T")
elif S.count("T") < S.count("A"):
  print("A")
else:
  print("A" if S[-1] == "T" else "T")
