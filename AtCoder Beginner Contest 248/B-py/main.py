A,B,K = map(int,input().split())
a = 0
while B > A:
  A *= K
  a += 1
print(a)
