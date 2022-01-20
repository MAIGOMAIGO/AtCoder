using System;
public static class main{
  public static void Main(string[] args){
    string[] NX = Console.ReadLine().Split(' ');
    int N = int.Parse(NX[0]);
    int X = int.Parse(NX[1]);
    int x = 0;
    for(int i=1;i<=N;i++){
      string[] VP = Console.ReadLine().Split(' ');
      int V = int.Parse(VP[0]);
      int P = int.Parse(VP[1]);
      x += (V * P);
      if(x>X*100){
      	Console.WriteLine(i);
        Environment.Exit(0);
      }
    }
    Console.WriteLine(-1);
  }
}
