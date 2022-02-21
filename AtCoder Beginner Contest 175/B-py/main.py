N = int(input())
L = list(map(int,input().split()))
L.sort()
a=0
for i in range(len(L)):
  for j in range(i):
    for k in range(j):
      if L[i]!=L[j] and L[j]!=L[k] and L[k]+L[j]>L[i]:
        a+=1
print(a)
