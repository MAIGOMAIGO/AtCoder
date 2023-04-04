N = int(input())
S = input()
x = 0
m = 0
for i in range(N):
  x = x + 1 if S[i] == "I" else x - 1
  m = x if x > m else m
print(m)
