# AtCoder Beginner Contest 195 B Many Oranges  
https://atcoder.jp/contests/abc195/tasks/abc195_b  
Python (3.8.2)で回答  

次のような判定問題を考えます。  
問題：1 個が A グラム以上 B グラム以下のみかんをちょうど N 個選んで W キログラムにすることはできるか？  
この問題に対する答えは、AN≤1000W≤BN が成り立つとき Yes、成り立たないとき No です。（最初に A グラムのみかんを N 個選んで、少しずつ大きなみかんと交換することをイメージしてみましょう）  
(解説参照)  
以上のことを参考にNa≤1000WA、1000WB≤Nbを求める。ちょうどWキロにならない時、Nb>NaであるためUNSATISFIABLEを出力。  
それ以外の場合はNb,Naを出力
