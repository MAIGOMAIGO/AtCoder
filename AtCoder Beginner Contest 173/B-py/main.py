AC,WA,TLE,RE = 0,0,0,0
for i in range(int(input())):
  S = input()
  if S == "AC":
    AC+=1
  elif S == "WA":
    WA+=1
  elif S == "TLE":
    TLE+=1
  elif S == "RE":
    RE+=1
print("AC x",AC)
print("WA x",WA)
print("TLE x",TLE)
print("RE x",RE)
