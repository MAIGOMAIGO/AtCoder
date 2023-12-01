N = int(input())
S = input()
L = [""]
p = 0
for i in range(N):
  if S[i] == "(":
    p += 1
    L.append(S[i])
  elif S[i] == ")":
    if p == 0:
      L[p] += S[i]
    else:
      L.pop(p)
      p -= 1
  else:
    L[p] += S[i]
s = ""
for i in L:
  s += i
print(s)
