N,S,K = map(int,input().split())
c = 0
for i in range(N):
  P,Q = map(int,input().split())
  c += P*Q
if S > c:
    c += K
print(c)
