S = ""
for i in range(10):
  S += input()
ac = S.find("#")
A = ac//10 + 1
C = ac%10 + 1
bd = 100 - S[::-1].find("#") - 1
B = bd//10 + 1
D = bd%10 + 1
print(A,B)
print(C,D)
