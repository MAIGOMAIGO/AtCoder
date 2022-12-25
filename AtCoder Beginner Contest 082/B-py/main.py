s = input()
t = input()
ls = [s[i] for i in range(len(s))]
lt = [t[i] for i in range(len(t))]
ls.sort()
lt.sort(reverse=True)
print("Yes") if ls < lt else print("No")
