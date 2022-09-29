N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
L = [abs(A-(T-x*0.006)) for x in H]
print(L.index(min(L))+1)
