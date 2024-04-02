N = int(input())
A = list(map(int,input().split()))
D = {A[i-1]:i for i in range(1,N+1)}
L = [D[-1]]
for i in range(N-1):
  L.append(D[L[-1]])
print(*L)
