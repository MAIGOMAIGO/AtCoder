import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int H = scan.nextInt();
      int W = scan.nextInt(); 
      String s = scan.nextLine();
      String[] S = new String[H]; 
      for(int i=0;i<H;i++){
        S[i] = scan.nextLine();
      }
      scan.close();
      
      int top = 0;
      for(int h=0;h<H-1;h++){
        int a=0;
        for(int w=0;w<W-1;w++){
          if(S[h].charAt(w) == '#')a++;
          if(S[h].charAt(w+1) == '#')a++;
          if(S[h+1].charAt(w) == '#')a++;
          if(S[h+1].charAt(w+1) == '#')a++;
          if((a==1)||(a==3))top++;
          a=0;
        }
      }
      System.out.println(top);
    }
}
