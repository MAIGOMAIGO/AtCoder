N,A,B = map(int,input().split())
c = 0
for i in range(1,N+1):
  s = str(i)
  L = [int(s[j]) for j in range(len(s))]
  if A <= sum(L) <= B:
    c += i
print(c)
