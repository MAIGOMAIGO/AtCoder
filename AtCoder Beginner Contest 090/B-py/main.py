A,B = map(int,input().split())
c = 0
for i in range(A,B+1):
  if str(i)[::-1] == str(i):
    c += 1
print(c)
