N = int(input())
S = input()
T = input()
S = S.replace("l","1")
S = S.replace("o","0")
T = T.replace("l","1")
T = T.replace("o","0")
if S == T:
  print("Yes")
else:
  print("No")
