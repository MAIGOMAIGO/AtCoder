import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    String[] S = new String[4];
    for(int i = 0; i < 4; i++){
      S[i] = scan.nextLine();
      for(int l=i; l > 0; l--){
        if(S[i].equals(S[l-1])){
          System.out.println("No");
          System.exit(0);
        }
      }
    }
    System.out.println("Yes");
  }
}
