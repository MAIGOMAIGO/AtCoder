H,W = map(int,input().split())
S,T = [],[]
for i in range(H):
  S.append(input())
for i in range(H):
  T.append(input())
s = list(map(list,zip(*S)))
t = list(map(list,zip(*T)))
s.sort()
t.sort()
print("Yes") if s == t else print("No")
