N = int(input())
S = input()
S1 = S[0]
for i in range(N):
  if i%2 == 0 and S1 != S[i]:
    print("No")
    exit(0)
  elif i%2 == 1 and S1 == S[i]:
    print("No")
    exit(0)
print("Yes")
