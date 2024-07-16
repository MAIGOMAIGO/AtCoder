N,K = map(int,input().split())
A = list(map(int,input().split()))
L = [i//K for i in A if i%K==0]
print(*L)