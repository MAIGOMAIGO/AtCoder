S = input()
if S[0] == "0":
  s = ""
  s += " " if S[6]=="0" else "1"
  s += " " if S[3]=="0" else "1"
  s += " " if S[7]=="0" and S[1]=="0" else "1"
  s += " " if S[4]=="0" else "1"
  s += " " if S[8]=="0" and S[2]=="0" else "1"
  s += " " if S[5]=="0" else "1"
  s += " " if S[9]=="0" else "1"
  L = list(map(str,s.split()))
  if len(L) >= 2:
    print("Yes")
    exit(0)
print("No")
