N = int(input())
S = input()
s = S.split('-')
L = [len(i) for i in s]
print(max(L)) if max(L) > 0 and '-' in S else print(-1)
