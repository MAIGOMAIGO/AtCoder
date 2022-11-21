## 標準入力

```python
# S 文字列
S = input()
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
# listをアンパックして半角スペース区切りで出力
print(*L)
```
## 変換

```python
# int to str
str(N)
# str to int
int(s)
# strlist to str
S = "区切り文字".join(L)
# otherlist to str
S = "区切り文字".join([str(i) for i in L])
# str to list[N]
L = S.split("区切り文字",N)
```

## 繰り返し上限アップ

```python
import sys
sys.setrecursionlimit(N)
```

## たまに使うやつ

```python
# List sort
L = [3, 1, 4, 5, 2]
L.sort() # [1, 2, 3, 4, 5]
L.sort(reverse=True) # [5, 4, 3, 2, 1]
L = sorted(L) # [1, 2, 3, 4, 5]
L = sorted(L, reverse=True) # [5, 4, 3, 2, 1]
# reverse str
S[::-1]
```

## 集合
```python
# 集合 重複無しにできたりソートされてたりする
s = set([5,3,2,4,3,2,9])
print(s) # {2, 3, 4, 5, 9}
# 追加
s.add(7)
s.add(5)
print(s) # {2, 3, 4, 5, 7, 9}
# 削除
s.discard(3)
s.discard(8) # 無くてもエラー出ない
print(s) # {2, 4, 5, 7, 9}
```

## 連想配列
```python
# キーに対応した値が返される、アイテムをlistなどにすることも可能
d = {'a':1,'b':5,3:'c'}
print(d) # {'a': 1, 'b': 5, 3: 'c'}
print(d['a']) # 1
print(d[3]) # c
# 追加
d['d'] = "hello"
print(d) # {'a': 1, 'b': 5, 3: 'c', 'd': 'hello'}
# 削除
d.pop(3)
print(d) # {'a': 1, 'b': 5, 'd': 'hello'}
```
