N = int(input())
s1 = ['H','D','C','S']
s2 = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
L = []
for i in range(N):
  S = input()
  if S[0] not in s1 or S[1] not in s2 or S in L:
    print("No")
    exit(0)
  L.append(S)
print("Yes")
