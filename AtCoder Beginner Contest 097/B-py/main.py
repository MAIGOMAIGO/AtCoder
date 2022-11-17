X = int(input())
L = [1]
for b in range(2,X+1):
  p = 2
  while b**p <= X:
    L.append(b**p)
    p+=1
print(max(L))
