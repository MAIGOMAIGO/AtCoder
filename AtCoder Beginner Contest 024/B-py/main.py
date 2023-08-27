N,T = map(int,input().split())
a,c = int(input()),0
for i in range(1,N):
  A = int(input())
  if a+T < A:
    c += T
  else:
    c += A-a
  a = A
print(c+T)
