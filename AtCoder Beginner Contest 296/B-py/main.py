for i in range(8):
  S = input()
  if "*" in S:
    x = "abcdefgh"
    y = "87654321"
    print(x[S.find("*")]+y[i])
    exit(0)
