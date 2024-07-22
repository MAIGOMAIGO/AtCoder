S = input()
T = input()
L = []
s = 0
for i in range(len(T)):
  if S[s] == T[i]:
    L.append(i+1)
    s += 1
  if len(S) <= s:
    break
print(*L)