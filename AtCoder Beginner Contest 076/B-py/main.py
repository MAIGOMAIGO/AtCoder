N = int(input())
K = int(input())
c = 1
for i in range(N):
  c = 2*c if 2*c <= c+K else c+K
print(c)
