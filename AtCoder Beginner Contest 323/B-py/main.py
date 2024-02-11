N = int(input())
D = {i+1:0 for i in range(N)}
for i in range(N):
  S = input()
  for j in range(N):
    D[i+1] += 1 if S[j] == "o" else 0
L = sorted(D.items(), key=lambda x:x[1], reverse=True)
print(" ".join([str(i[0]) for i in L]))
