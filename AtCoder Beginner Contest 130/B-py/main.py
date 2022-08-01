N,X = map(int,input().split())
L = list(map(int,input().split()))
c,a = 1,0
for i in L:
  a += i
  if a <= X:
    c+= 1 
  else:
    break
print(c)
