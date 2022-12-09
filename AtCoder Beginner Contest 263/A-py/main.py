ABCDE = list(map(int,input().split()))
ABCDE.sort()
if ((ABCDE[0]==ABCDE[1]==ABCDE[2] and ABCDE[3]==ABCDE[4]) or (ABCDE[0]==ABCDE[1] and ABCDE[2]==ABCDE[3]==ABCDE[4])) and ABCDE[0] != ABCDE[4]:
  print("Yes") 
else:
  print("No")
