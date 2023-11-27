n = int(input())
a = list(map(int,input().split()))
L = [0,1,0,1,2,3,0,1,0]
c = 0
for i in a:
  c += L[i-1]
print(c)
