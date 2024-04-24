A = []
while True:
  a = int(input())
  A.append(a)
  if a == 0:
    break

for i in A[::-1]:
  print(i)
