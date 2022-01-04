N = int(input())
l = (len(str(N))-1)/3
c=0
for i in reversed(range(0,int(l)+1)):
  if i == 0:
    break
  c += (N - (1000**i - 1))
print(c)
