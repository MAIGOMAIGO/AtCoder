V,A,B,C = map(int,input().split())
p = -1
while V>=0:
  p = (p+1)%3
  V-= A if p==0 else B if p==1 else C
print("F") if p==0 else print("M") if p==1 else print("T")
