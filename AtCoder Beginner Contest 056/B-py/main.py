W,a,b = map(int,input().split())
print(b-a-W) if b > a+W else print(a-b-W) if a > b+W else print(0)
