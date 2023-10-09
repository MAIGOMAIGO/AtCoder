S = input()
N = int(input())
for i in range(N):
  l,r = map(int,input().split())
  rv = S[l-1:r]
  S = S[:l-1] + rv[::-1] + S[r:]
print(S)
