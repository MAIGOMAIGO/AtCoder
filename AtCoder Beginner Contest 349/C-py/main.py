S = input()
T = input().lower()
if T[-1] == "x":
  T = T[:2]
l,j = len(T),0
for i in range(len(S)):
  if S[i] == T[j]:
    j += 1
    if l == j:
      print("Yes")
      exit(0)
print("No")