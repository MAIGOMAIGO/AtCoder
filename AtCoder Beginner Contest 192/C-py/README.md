# AtCoder Beginner Contest 192 C Kaprekar Number  
https://atcoder.jp/contests/abc192/tasks/abc192_c  
Python (3.8.2)で回答  

今回の問題はf(x)を繰り返し呼び出す必要があったため再帰的な関数を作った。  
制約より再帰する最大回数は$ 10^{5} $だがPythonで同じ関数を呼び出すのはデフォルトで1000回までと設定されている。  
そのため最初に`sys.setrecursionlimit(1000000)`をして再帰に十分な余裕を持たせる必要がある。  

g1、g2の数字を順番を並び替えるのは文字の配列にして`sorted()`を使ってそれぞれ並び替えた。  
後は目的の通り計算を繰り返し結果を出力
