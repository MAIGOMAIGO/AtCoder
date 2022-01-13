# AtCoder Beginner Contest 202 A Three Dice  
https://atcoder.jp/contests/abc202/tasks/abc202_a  
C++ (Clang 10.0.0)で回答  

サイコロは出た目とその裏の目を足すと必ず7になるように作られてるので、(出た目+出た目の裏)×3つのダイス=21になる。  
なので21 - 出た目の合計 = 出た目の裏の合計である。
