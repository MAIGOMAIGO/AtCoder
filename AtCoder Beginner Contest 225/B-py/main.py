N = int(input())
A,B = map(int,input().split())
for i in range(N-2):
  a,b = map(int,input().split())
  if A!=a and A!=b:
    A = -1
  if B!=a and B!=b:
    B = -1
  if A == -1 and B == -1:
    break
print("Yes") if A != -1 or B != -1 else print("No")
