N,D,P = map(int,input().split())
F = list(map(int,input().split()))
c = 0
F.sort()
avg = P/D
high,low = [],[]
for i in F:
  if i >= avg:
    high.append(i)
  else:
    low.append(i)
if len(high) > 0:
  c += (len(high)//D)*P
  s = len(high)%D
  if len(low) >= D-s:
    ds = len(low)-(D-s)
    hlow = low[ds:]
    c += sum(low[:ds])
    hlow += high[:s]
    if sum(hlow) >= P:
      c += P
    else:
      c += sum(hlow)
  else:
    low += high[:s]
    if sum(low) >= P:
      c += P
    else:
      c += sum(low)
else:
  c += sum(low)
print(c)
