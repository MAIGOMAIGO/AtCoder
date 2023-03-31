def f(n):
  return 1 if n==0 else n*f(n-1)
N = int(input())
print(f(N))
