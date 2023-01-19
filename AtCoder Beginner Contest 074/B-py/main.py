N = int(input())
K = int(input())
x = list(map(int,input().split()))
c = 0
for i in x:
  c += abs(K-i) if abs(K-i) < i else i
print(2*c)
