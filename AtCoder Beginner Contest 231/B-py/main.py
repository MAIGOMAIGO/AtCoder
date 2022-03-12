import statistics
S = []
for i in range(int(input())):
  S.append(input())
print(statistics.mode(S))
