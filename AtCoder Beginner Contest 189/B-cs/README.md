# AtCoder Beginner Contest 189 B Alcoholic  
https://atcoder.jp/contests/abc189/tasks/abc189_b  
C# (.NET Core 3.1.201)で回答  

アルコールの摂取量が越えるまで足していき越えなければ`-1`を出せば良いが、
浮動小数点の計算は一般に誤差を含むので整数のみで計算できるように式変形する必要がある  
今回はPを100で割る代わりにXを100倍した。
