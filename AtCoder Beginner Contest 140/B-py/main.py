N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
T = 0
for i in range(len(A)):
  T += B[A[i]-1]
  if i >= 1 and A[i] == A[i-1] + 1:
    T += C[A[i-1]-1]
print(T)
