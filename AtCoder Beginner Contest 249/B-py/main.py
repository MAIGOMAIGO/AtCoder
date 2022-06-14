S = input()
if len(set(S)) == len(S):
  if not S.islower() and not S.isupper():
    print("Yes")
    exit()
print("No")
