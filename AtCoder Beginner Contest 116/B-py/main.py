s = int(input())
L = [s]
c = 1
while(True):
  if s%2 == 0:
    s /= 2
  else:
    s = 3*s + 1
  c += 1
  if s in L:
    break
  else:
    L.append(s)
print(c)
