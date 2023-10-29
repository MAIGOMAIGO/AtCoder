S,T = input(),input()
SD,TD = dict(),dict()
for i in range(len(S)):
  if S[i] in SD:
    SD[S[i]] += 1
  else:
    SD[S[i]] = 1
  if T[i] in TD:
    TD[T[i]] += 1
  else:
    TD[T[i]] = 1
sd,td = dict(),dict()
cs,ct = 0,0
for i in SD.keys():
  if i == '@':
    sd[i] = SD[i]
  elif i in TD and TD[i] != SD[i]:
    if TD[i] > SD[i]:
      td[i] = TD[i] - SD[i]
      ct += td[i]
    elif TD[i] < SD[i]:
      sd[i] = SD[i] - TD[i]
      cs += sd[i]
  elif i not in TD:
    sd[i] = SD[i]
    cs += sd[i]
for i in TD.keys():
  if i == '@':
    td[i] = TD[i]
  elif i not in SD:
    td[i] = TD[i]
    ct += td[i]
if '@' not in sd:
  sd['@'] = 0
if '@' not in td:
  td['@'] = 0
s = ["a","t","c","o","d","e","r"]
for i in sd.keys():
  if i != '@' and i not in s:
    print("No")
    exit(0)
for i in td.keys():
  if i != '@' and i not in s:
    print("No")
    exit(0)
print("Yes") if ct <= sd['@'] and cs <= td['@'] else print("No")
