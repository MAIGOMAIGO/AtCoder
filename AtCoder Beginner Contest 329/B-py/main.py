N = int(input())
A = set(list(map(int,input().split())))
L = sorted(A,reverse=True)
print(L[1])
