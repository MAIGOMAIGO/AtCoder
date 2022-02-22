N = int(input())
name = []
for S in range(N):
  name.append(input())
print("Yes") if len(name) != len(set(name)) else print("No")
