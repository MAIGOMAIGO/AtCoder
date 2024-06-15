import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int A = sc.nextInt();
    int B = sc.nextInt();
    int C = sc.nextInt();
    int count = 0;
    while(true){
      if(A==B && B==C && A==C){
        System.out.println(count);
        break;
      }
      if(A <= B && A <= C){
        if(B == C){
          A += 2;
        }else if(B > C){
          A++;C++;
        }else if(B < C){
          A++;B++;
        }
      }else if(B <= A && B <= C){
        if(A == C){
          B += 2;
        }else if(A > C){
          B++;C++;
        }else if(A < C){
          B++;A++;
        }
      }else if(C <= A && C <= B){
        if(A == B){
          C += 2;
        }else if(A > B){
          C++;B++;
        }else if(A < B){
          C++;A++;
        }
      }
      count++;
    }
  }
}