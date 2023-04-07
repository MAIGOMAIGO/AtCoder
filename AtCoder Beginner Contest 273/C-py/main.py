N = int(input())
A = list(map(int,input().split()))
a = {}
for i in A:
  if i not in a:
    a[i] = 1
  else:
    a[i] += 1
a = sorted(a.items(),reverse=True)
for i in range(len(a)):
  print(a[i][1])
for i in range(N-len(a)):
  print(0)
