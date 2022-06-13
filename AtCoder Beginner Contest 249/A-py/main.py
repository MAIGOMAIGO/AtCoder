A,B,C,D,E,F,X = map(int,input().split())
TAKA = AOKI = 0
for i in range(X):
  TAKA += B if i%(A+C) < A else 0
  AOKI += E if i%(D+F) < D else 0
print("Draw") if TAKA == AOKI else print("Takahashi") if TAKA > AOKI else print("Aoki")
