N = int(input())
p = []
for i in range(N):
  p.append(int(input()))
pm = max(p)//2
print(sum(p)-pm)
