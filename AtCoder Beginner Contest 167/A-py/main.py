S = input()
T = input()
print("Yes") if S == T[:len(S)] and len(S)+1==len(T) else print("No")
