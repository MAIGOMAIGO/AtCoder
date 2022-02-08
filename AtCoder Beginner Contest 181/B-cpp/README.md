# AtCoder Beginner Contest 181 B Trapezoid Sum  
https://atcoder.jp/contests/abc181/tasks/abc181_b  
C++ (GCC 9.2.1) で回答  

普通に一つずつ足していくと時間が足りないので、計算式を作って時間短縮する。  
(B-A+1)×((A+B)/2)のようにAからBまでの数×AとBの平均値をすると求められる。  
後はN回分この作業を繰り返すだけ。
