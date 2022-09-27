S = input()
L = []
for i in range(len(S)-2):
  L.append(abs(753-int(S[i:i+3])))
print(min(L))
