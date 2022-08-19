S = input()
if 0 < int(S[:2]) <= 12 and 0 < int(S[2:]) <= 12:
  print("AMBIGUOUS")
elif 0 < int(S[:2]) <= 12 and (0 == int(S[2:]) or int(S[2:]) > 12):
  print("MMYY")
elif (0 == int(S[:2]) or int(S[:2]) > 12) and 0 < int(S[2:]) <= 12:
  print("YYMM")
else:
  print("NA")
