w = input()
D = {}
for i in range(len(w)):
  if w[i] in D:
    D[w[i]] += 1
  else:
    D[w[i]] = 1
for k,i in D.items():
  if i%2 == 1:
    print("No")
    exit(0)
print("Yes")
