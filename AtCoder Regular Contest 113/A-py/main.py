K = int(input())
x = 0
for a in range(1,K+1):
  for b in range(1,K//a+1):
    x+=(K//(a*b))
print(x)
