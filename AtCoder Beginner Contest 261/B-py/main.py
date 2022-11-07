N = int(input())
A = []
for i in range(N):
  A.append(input())
for i in range(N):
  L = ['L' if j[i] == 'W' else 'W' if j[i] == 'L' else j[i] for j in A]
  if "".join(L) != A[i]:
    print("incorrect")
    exit()
print("correct")
