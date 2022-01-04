A,B,W=map(int,input().split())
m=int(1000*W/A)
l=1000*W/B
if l%1 == 0:
  l=int(l)
else:
  l=int(l+1)
if l>m:
  print("UNSATISFIABLE")
else:
  print(l,m)
