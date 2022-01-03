public static class main
{
  public static void Main(string[] args)
  {
    var input = System.Console.ReadLine().Split(' ');
    var M = System.Int32.Parse(input[0]);
    var H = System.Int32.Parse(input[1]);
    if(H%M == 0){
      System.Console.WriteLine("Yes");
    }
    else{
      System.Console.WriteLine("No");
    }
  }
}
