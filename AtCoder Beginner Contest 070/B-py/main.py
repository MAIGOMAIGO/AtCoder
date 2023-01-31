A,B,C,D = map(int,input().split())
L1 = list(range(A,B+1))
L2 = list(range(C,D+1))
L = L1+L2
S = set(L)
print(len(L)-len(S)-1) if len(S) < len(L) else print(0)
