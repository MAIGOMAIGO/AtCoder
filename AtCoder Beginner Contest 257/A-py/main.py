N,X = map(int,input().split())
s = 'A'
S = ""
for i in range(26):
  S += chr((ord(s)+i))*N
print(S[X-1])
