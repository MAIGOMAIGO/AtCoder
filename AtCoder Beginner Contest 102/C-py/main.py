N = int(input())
A = list(map(int,input().split()))
for i in range(N):
  A[i] -= (i+1)
a = sorted(A,key=int)
b = 0
if N%2 == 1:
  b = a[int(N/2)]
else:
  b = (a[int(N/2-1)] + a[int(N/2)]) / 2
x=0
for n in range(N):
  x += abs(A[n]-b)
print(int(x))