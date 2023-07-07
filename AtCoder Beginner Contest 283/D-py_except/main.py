S = input()
s = set()
for i in S:
  if i == '(':
    1;
  elif i == ')':
    s = set()
  else:
    if i in s:
      print("No")
      exit(0)
    s.add(i)
print("Yes")
