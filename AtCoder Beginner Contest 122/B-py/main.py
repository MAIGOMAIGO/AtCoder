S = input()
ACGT = ['A','C','G','T']
for i in range(len(S)):
  if not S[i] in ACGT:
    S = S[:i] + " " + S[i+1:]
L = list(map(str,S.split()))
L = [len(i) for i in L]
print(max(L) if L != [] else 0)
