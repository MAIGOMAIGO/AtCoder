N = int(input())
for i in range(25+1):
  for j in range(15):
    if i*4+j*7 == N:
      print("Yes")
      exit(0)
print("No")
