N,A,B = map(int,input().split())
n = N%(A+B)
AB = n if A > n else A
print((N//(A+B))*A+AB)
