N = int(input())
p = list(map(int,input().split()))
ps = sorted(p)
L = [i for i in range(N) if p[i]!=ps[i]]
print("YES") if len(L) <= 2 else print("NO")
