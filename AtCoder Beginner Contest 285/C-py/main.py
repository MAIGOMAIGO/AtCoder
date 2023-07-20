S = input()
D = {chr(65+i):i+1 for i in range(26)}
c = 0
RS = S[::-1]
for i in range(len(S)):
  c += 26**i * D[RS[i]]
print(c)
