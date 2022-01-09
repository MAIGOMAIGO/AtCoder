N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
x = min(B) - max(A) + 1
if x < 0:
  x = 0
print(x)
