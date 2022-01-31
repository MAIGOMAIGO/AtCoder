# AtCoder Beginner Contest 193 C Unexpressed  
https://atcoder.jp/contests/abc193/tasks/abc193_c  
C# (.NET Core 3.1.201)で回答  

問題のお通りに計算しようとすると、Nの最大値が10,000,000,000であるため当然間に合わない。  
今回求める値はa^bと表せないものなので逆にa^bと表せる数を数えていく。  
aの最大値は√N以下であるため、√N以下でa^bで表せる数以外をN以下のの範囲で累乗していく。  
√N以下でa^bで表せる数は配列で記憶しとくと検索に時間がかかったのでHashSetを使って保存した。  
以上のことを行い最後にNからa^bで表せる数を引くと答えになる。
