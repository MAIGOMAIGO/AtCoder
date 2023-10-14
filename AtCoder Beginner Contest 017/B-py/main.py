X = input()
L = ['ch','o','k','u']
for i in L:
  X = X.replace(i,'')
print("YES") if len(X) == 0 else print("NO")
