S = input()
T = input()
DS = [S[0],1]
for i in range(1,len(S)):
  if DS[-2] == S[i]:
    DS[-1] += 1
  else:
    DS.append(S[i])
    DS.append(1)
DT = [T[0],1]
for i in range(1,len(T)):
  if DT[-2] == T[i]:
    DT[-1] += 1
  else:
    DT.append(T[i])
    DT.append(1)
c = 0
if len(DS) == len(DT):
  for i in range(len(DS)):
    if i%2 == 0:
      if DS[i] == DT[i]:
        if DS[i+1] <= DT[i+1]:
          if DS[i+1] > 1:
          	c += 1
          else:
            if DS[i+1] == DT[i+1]:
              c += 1
print("Yes") if c*2 == len(DS) else print("No")
