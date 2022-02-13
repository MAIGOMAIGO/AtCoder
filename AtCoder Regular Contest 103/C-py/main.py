import collections as col
n = int(input())
v = list(map(int,input().split()))
v1,v2 = [],[]
for i in range(n):
  v1.append(v[i]) if i%2 == 0 else v2.append(v[i])
c1 = col.Counter(v1)
c2 = col.Counter(v2)
if c1.most_common()[0][0] != c2.most_common()[0][0]:
  A = c1.most_common()[0][1] + c2.most_common()[0][1]
  print(n-(c1.most_common()[0][1] + c2.most_common()[0][1]))
elif c1.most_common()[0][1] + c2.most_common()[0][1] == n:
  print(int(n/2))
else:
  if c1.most_common()[0][1] == c2.most_common()[0][1]:
    if c1.most_common()[1][1] > c2.most_common()[1][1]:
      print(n-(c1.most_common()[1][1] + c2.most_common()[0][1]))
    else:
      print(n-(c1.most_common()[0][1] + c2.most_common()[1][1]))
  elif c1.most_common()[0][1] > c2.most_common()[0][1]:
    print(n-(c1.most_common()[0][1] + c2.most_common()[1][1]))
  else:
    print(n-(c1.most_common()[1][1] + c2.most_common()[0][1]))
