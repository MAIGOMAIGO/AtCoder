S = input()+input()
if S.count("#")>=3:
  print("Yes")
elif S.count("#.#")>=1 or S=="##.." or S=="..##":
  print("Yes")
else:
  print("No")
