N = int(input())
S = []
for i in range(N):
  S.append(input())
for i in range(N-1):
  for j in range(i+1,N):
    s = S[i] + S[j]
    rs = S[j] + S[i]
    if s == s[::-1] or rs == rs[::-1]:
      print("Yes")
      exit(0)
print("No")
