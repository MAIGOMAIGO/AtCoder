N = int(input())
S = input()
s = ""
for i in range(len(S)):
  s += chr(ord(S[i])+N-26) if ord(S[i])+N > 90 else chr(ord(S[i])+N)
print(s)
