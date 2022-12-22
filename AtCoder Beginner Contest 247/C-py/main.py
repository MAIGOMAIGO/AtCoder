def f(n):
  if n > 1:
    return f(n-1) + [n] + f(n-1)
  else:
    return [1]
N = int(input())
print(*f(N))
