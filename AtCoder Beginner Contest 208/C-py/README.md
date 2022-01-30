# AtCoder Beginner Contest 208 C Fair Candy Distribution  
https://atcoder.jp/contests/abc208/tasks/abc208_c  
Python (3.8.2)で回答  

国民に配られるお菓子の数はを考えると国民番号の小さい順からa1～aのN%KまではN//K+1であり、それ以外はN//Kである。  
最初に与えられるaでは小さい順ではないのでソートしたAを用意し、N%K番目の値を把握する。  
これにより、aに与えられた国民番号の数字が整列されたAのN%K番目の数字より小さい数字であった時にN//K+1を表示し、それ以外はN//Kを表示すればいい。
