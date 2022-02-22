N = float(input())
if (N*10)%10 <= 2:
  print("%d-" % int(N))
elif (N*10)%10 >= 7:
  print("%d+" % int(N))
else:
  print(int(N))
