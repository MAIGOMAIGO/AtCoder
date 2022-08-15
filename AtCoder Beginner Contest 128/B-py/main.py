N = int(input())
SP = []
for i in range(N):
  SP.append(input())
sp = sorted(SP)
for i in range(N-1):
  for j in range(i,N):
    iS,iP = map(str,sp[i].split())
    jS,jP = map(str,sp[j].split())
    if iS == jS and int(iP) < int(jP):
      sp[i],sp[j] = sp[j],sp[i]
for i in sp:
  print(SP.index(i)+1)
