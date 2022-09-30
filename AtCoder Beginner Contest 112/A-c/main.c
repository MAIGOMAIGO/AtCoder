#include <stdio.h>
#define SUM(A,B) (A+B)
int main(void){
  int N;scanf("%d",&N);
  if(N==1){
    printf("Hello World");
  }else{
    int A,B;scanf("%d\n%d",&A,&B);
    printf("%d",SUM(A,B));
  }
  return 0;
}
