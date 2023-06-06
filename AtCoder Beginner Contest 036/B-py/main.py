N = int(input())
s = []
for i in range(N):
  s.append(input())
L = list(map(list,zip(*s)))
for i in L:
  print("".join(i[::-1]))
