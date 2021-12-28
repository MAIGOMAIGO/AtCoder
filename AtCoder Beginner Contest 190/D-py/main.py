N=int(input())
z=0
n=1
while (n*n)<=(2*N):
  if (N*2)%n == 0:
    a = n-(int((2*N)/n))+1
    if a%2 == 0:
      z+=1
  n+=1
print(z*2)
