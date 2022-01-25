## 標準入力

```python
# N 整数
N = int(input())
# N M 整数
N,M = map(int,input().split())
# A1 A2 A3...An 整数
A = list(map(int,input().split()))
```

## 標準出力

```python
# Yes 文字列
print("Yes")
# N 整数
print(N)
# if文
print("Yes") if N == 0 else print("No")
```
## 変換

```python
# int to str
str(N)
# str to int
int(s)
# list to str
S = "区切り文字".join(L)
# str to list[N]
L = S.split("区切り文字",N)
```

## 繰り返し上限アップ

```python
import sys
sys.setrecursionlimit(N)
```
