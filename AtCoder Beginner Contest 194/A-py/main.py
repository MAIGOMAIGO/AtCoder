AB = list(map(int,input().split()))
if (AB[0]+AB[1] >= 15) and (AB[1] >= 8):
  print(1)
elif (AB[0]+AB[1] >= 10) and (AB[1] >= 3):
  print(2)
elif AB[0]+AB[1] >= 3:
  print(3)
else:
  print(4)
