N = int(input())
LR = []
for i in range(N):
  LR.append(list(map(int,input().split())))
LR.sort()
flag = True
while flag:
  flag = False
  for i in range(1,len(LR)):
    if LR[i][0] <= LR[i-1][1] and LR[i-1]!=[0,0]:
      if LR[i][1] >= LR[i-1][1]:
        LR[i-1][1] = LR[i][1]
      LR[i] = [0,0]
      flag = True
  LR = [i for i in LR if i!=[0,0]]
for i in LR:
  print(i[0],i[1])
