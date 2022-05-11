N,M = map(int,input().split())
A = list(map(int,input().split()))
t = sum(A)/(4*M)
L = [a for a in A if a >= t]
print("Yes") if len(L) >= M else print("No")
