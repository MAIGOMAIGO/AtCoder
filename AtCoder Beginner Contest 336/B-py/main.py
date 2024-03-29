N = int(input())
b = bin(N)
c = 0
for i in str(b)[::-1]:
  if i == "0":
    c += 1
  else:
    break
print(c)
