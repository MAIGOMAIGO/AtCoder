N = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
Alice,Bob = 0,0
for idx,item in enumerate(a):
  if idx%2==0:
    Alice += item
  else:
    Bob += item
print(Alice-Bob)
