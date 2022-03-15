L,R = map(int,input().split())
S = input()
SR = S[L-1:R]
print(S[:L-1]+SR[::-1]+S[R:])
