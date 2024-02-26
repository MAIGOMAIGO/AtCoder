B = int(input())
a = 1
while(B > a**a):
  a += 1
print(a if B == a**a else -1)
