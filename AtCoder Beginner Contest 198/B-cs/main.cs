public static class main
{ 
  public static void Main(string[] args)
  {
    string N = System.Console.ReadLine();
    for(int i=N.Length-1;i>=0;i--){
      if(N.Substring(i,1)!="0"){
        if(i < N.Length-1){
          N = N.Remove(i+1);
        }
        break;
      }
    }
    for(int i=0;i<N.Length/2;i++){
      if(N.Substring(i,1) != N.Substring(N.Length-i-1,1)){
        System.Console.WriteLine("No");
        System.Environment.Exit(0);
      }
    }
    System.Console.WriteLine("Yes");
  }
}
