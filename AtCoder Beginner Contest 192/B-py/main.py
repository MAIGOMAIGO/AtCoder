import sys
S = input()
for i in range(len(S)):
  if (i%2==1 and S[i].islower()) or (i%2==0 and S[i].isupper()):
    print('No')
    sys.exit()
print('Yes')
