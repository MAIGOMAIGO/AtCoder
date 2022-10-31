S = input()
N = int(S)
s = 0
for i in range(len(S)):
  s += int(S[i])
print("Yes") if N%s == 0 else print("No")
