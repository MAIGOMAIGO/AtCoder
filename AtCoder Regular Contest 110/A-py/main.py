import math
from functools import reduce

def my_lcm(x,y):
  return (x*y)//math.gcd(x,y)

N = int(input())
L = list(range(2,N+1))
print(reduce(my_lcm, L, 1)+1)
