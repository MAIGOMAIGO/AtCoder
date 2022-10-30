S = input()
c = 0
for i in range(4):
  c += 1 if S[i] == '+' else -1
print(c)
