N = int(input())
A = list(map(int,input().split()))
A = [i for i in A if i%2==0]
for a in A:
  if a%3 != 0 and a%5 != 0:
    print("DENIED")
    exit()
print("APPROVED")
