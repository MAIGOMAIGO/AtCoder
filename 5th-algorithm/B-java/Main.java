import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int N = Integer.parseInt(scan.nextLine());
    String S = scan.nextLine();
    String T = new String();
    T += S.charAt(0);
    for(int i=1;i<N;i++){
      for(int s=0;s<T.length();s++){
        if(T.charAt(s) == S.charAt(i)){
          T = T.replace(String.valueOf(S.charAt(i)),"");
          break;
        }
      }
      T += S.charAt(i);
    }
    System.out.println(T);
  }
}
