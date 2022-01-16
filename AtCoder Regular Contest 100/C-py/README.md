# AtCoder Regular Contest 100 C Linear Approximation  
https://atcoder.jp/contests/arc100  
Python (3.8.2)で回答  

すぬけ君の悲しさの値が最小値になるためには、abs(An-(b+N))がなるべく0に近づくようにする。  
bは自由な値なのでそれぞれ確定する数字からbを割り出す。  
A[i]とNは出てくるので、abs(An-(b+N))をabs((An-N)-b)で計算する。(An-N)配列の中央値で引くと悲しさの値が最小値になる。  
そのため(An-N)をソートし、中央値を求めbに代入。あとは計算していき、結果を出力する。
