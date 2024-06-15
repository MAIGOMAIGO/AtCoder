N = int(input())
D = {'M':0,'A':0,'R':0,'C':0,'H':0}
for i in range(N):
  S = input()
  if S[0] in D:
    D[S[0]] += 1
L = ['M','A','R','C','H']
c = 0
for i in range(3):
  for j in range(i+1,4):
    for k in range(j+1,5):
      c += D[L[i]] * D[L[j]] * D[L[k]]
print(c)