H,W = map(int,input().split())
R,C = map(int,input().split())
a = 0
if R-1 > 0:
  a += 1
if R+1 <= H:
  a += 1
if C-1 > 0:
  a += 1
if C+1 <= W:
  a += 1
print(a)
