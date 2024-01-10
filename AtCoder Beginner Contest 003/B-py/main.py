S = input()
T = input()
L = ['a','t','c','o','d','e','r','@']
for i in range(len(S)):
  if S[i] != T[i] and S[i] != '@' and T[i] != '@' \
  or S[i] == '@' and T[i] not in L or T[i] == '@' and S[i] not in L:
    print("You will lose")
    exit(0)
print("You can win")
