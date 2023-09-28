N,X = map(int,input().split())
A = list(map(int,input().split()))
S = set(A)
for i in A:
  if i+X in S or i-X in S:
    print("Yes")
    exit(0)
print("No")
