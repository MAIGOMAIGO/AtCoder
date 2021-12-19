public static class main
{ 
  public static void Main(string[] args)
  {
    string line = System.Console.ReadLine();
    int N = System.Int32.Parse(line);
    string str = null;
    
    for(int i=2;i>=0;i--){
      int S = (int)(N / System.Math.Pow(36,i));
      N = N - (int)(S * System.Math.Pow(36,i));
      if(S>=10){
        str += ((char)(S+55)).ToString();
      }else{
        str += S.ToString();
      }
    }
    if(str[0]=='0'){
      if(str[1]=='0'){
        str = str.Substring(1);
      }
      str = str.Substring(1);
    }
    System.Console.WriteLine(str);
  }
}
