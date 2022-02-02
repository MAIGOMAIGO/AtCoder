#include <stdio.h>
int main(){
  int A,B;
  scanf("%d %d",&A,&B);
  if(A+B >= 15 && B >= 8){
    printf("1");
  }else if(A+B >= 10 && B >= 3){
    printf("2");
  }else if(A+B >= 3){
    printf("3");
  }else{
    printf("4");
  }
  return 0;
}
