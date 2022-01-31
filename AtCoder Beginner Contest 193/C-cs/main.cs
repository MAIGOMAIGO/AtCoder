using System;
using System.Collections.Generic;
public static class main{
  public static void Main(string[] args){
    long N = long.Parse(Console.ReadLine());
    long X = 0;
    HashSet<long> H = new HashSet<long>();
    for(long i=2;i*i<=N;i++){
      if(H.Contains(i)){
        continue;
      }
      for(long l=2;Math.Pow(i,l)<=N;l++){
        H.Add((long)Math.Pow(i,l));
        X++;
      }
    }
    Console.WriteLine(N-X);
  }
}
