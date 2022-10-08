N = int(input())
S = [input()]
for i in range(N-1):
  s = input()
  if (s in S) or (S[-1][-1] != s[0]):
    print("No")
    exit(0)
  S.append(s)
print("Yes")
