X,Y = map(int,input().split())
c = 1
while X*2 <= Y:
  X *= 2
  c += 1
print(c)
