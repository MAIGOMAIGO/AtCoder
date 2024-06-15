S = input()
K = int(input())
if len(S) >= K:
  for i in range(K):
    if S[i] != "1":
      print(S[i])
      exit(0)
  print(S[K-1])
else:
  for i in S:
    if i != "1":
      print(i)
      exit(0)