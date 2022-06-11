N = int(input())
S,T = map(str,input().split())
ST = ""
for i in range(N):
  ST += S[i]+T[i]
print(ST)
