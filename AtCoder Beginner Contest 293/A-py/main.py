S = input()
s = ""
for i in range(len(S)//2):
  s += S[2*i+1] + S[2*i]
print(s)
