b = input()
if b == "A" or b == "T":
  b = "T" if b == "A" else "A"
else:
  b = "G" if b == "C" else "C"
print(b)
