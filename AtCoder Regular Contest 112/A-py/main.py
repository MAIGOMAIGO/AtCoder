T = int(input())
for i in range(T):
  L,R = map(int,input().split())
  l = R-L*2
  print(0) if l < 0 else print((l+1)*(l+2)//2)
