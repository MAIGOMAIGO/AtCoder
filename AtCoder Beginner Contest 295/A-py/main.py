N = int(input())
W = input().split()
L = ["and","not","that","the","you"]
for i in W:
  if i in L:
    print("Yes")
    exit(0)
print("No")
