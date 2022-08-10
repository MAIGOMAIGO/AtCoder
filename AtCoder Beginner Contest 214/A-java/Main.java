import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int N = Integer.parseInt(scan.nextLine());
    if(N<=125){
      System.out.println(4);
    }else if(N>=212){
      System.out.println(8);
    }else{
      System.out.println(6);
    }
  }
}
