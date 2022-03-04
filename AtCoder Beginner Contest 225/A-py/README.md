# AtCoder Beginner Contest 225 A Distinct Strings  
https://atcoder.jp/contests/abc225/tasks/abc225_a  
Python (3.8.2)で回答  

与えられた文字列から`set()`で同じ文字を消し、`len()`で文字数を取得。  
`list(range(文字数+1))`で文字数から0までの数字の配列を作成し、`sum()`で合計値を出せば答え。  
これなら文字数が3文字じゃなくても対応できるはず。
