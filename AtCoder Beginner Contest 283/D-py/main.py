S = input()
L = [[] for i in range(len(S))] 
s = set()
p = 0
for i in S:
  if i == '(':
    p += 1
  elif i == ')':
    for j in L[p]:
      s.discard(j)
    L[p].clear()
    p -= 1
  else:
    if i in s:
      print("No")
      exit(0)
    s.add(i)
    L[p].append(i)
if p == 0:
  print("Yes")
else:
  print("No")
