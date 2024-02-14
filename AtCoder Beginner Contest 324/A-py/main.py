N = int(input())
A = list(map(int,input().split()))
for i in range(1,N):
  if A[0] != A[i]:
    print("No")
    exit(0)
print("Yes")
