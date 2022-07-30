N,L = map(int,input().split())
if L >= 0:
  print(sum(list(range(L+1,L+N))))
elif L <= 0 and L+N-1 >= 0:
  print(sum(list(range(L,L+N))))
else:
  print(sum(list(range(L,L+N-1))))
