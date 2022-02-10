N = int(input())
i=0
a='No'
for n in range(N):
  D1,D2 = map(int,input().split())
  if D1 == D2:
    i+=1
  else:
    i=0
  if i >= 3:
    a = 'Yes'
    break
print(a)
