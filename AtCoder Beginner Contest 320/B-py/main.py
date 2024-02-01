S = input()
ans = 0
size = len(S)
for i in range(size):
  for j in range(i+1):
    s = S[j:j+size-i]
    if s == s[::-1]:
      ans = size-i
      print(ans)
      exit(0)
