public static class main
{ 
  public static void Main(string[] args)
  {
    string S = System.Console.ReadLine();
    string s = "";
    for(int i = S.Length - 1; i >= 0; i--)
    {
      if(S[i] == '6')
      {
        s += '9';
      }
      else if(S[i] == '9')
      {
        s += '6';
      }
      else
      {
        s += S[i];
      }
    }
    System.Console.WriteLine(s);
  }
}
