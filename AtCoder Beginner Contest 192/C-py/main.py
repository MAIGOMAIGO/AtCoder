import sys
def f(a,i):
  if i<1:
    return a
  ai = f(a,i-1)
  g1 = int("".join(sorted(list(str(ai)),reverse=True)))
  g2 = int("".join(sorted(list(str(ai)))))
  return g1-g2
sys.setrecursionlimit(1000000)
NK = list(map(int, input().split()))
N = NK[0]
K = NK[1]
a = f(N,K)
print(a)
