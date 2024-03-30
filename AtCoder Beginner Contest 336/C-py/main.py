N = int(input()) - 1
L = []
while N >= 5:
  L.append(N%5)
  N //= 5
L.append(N)
l = ["0","2","4","6","8"]
S = ""
for i in L[::-1]:
  S += l[i]
print(S)
