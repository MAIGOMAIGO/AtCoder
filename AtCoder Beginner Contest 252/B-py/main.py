N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = [i+1 for i in range(N) if max(A)==A[i]]
for i in a:
  if i in B:
    print("Yes")
    exit()
print("No")
