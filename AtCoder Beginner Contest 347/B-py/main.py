S = input()
s = set()
for i in range(len(S)):
  for j in range(len(S)-i):
    s.add(S[j:j+i+1])
print(len(s))