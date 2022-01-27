#include <stdio.h>
int main(){
  int A,B;
  scanf("%d %d",&A,&B);
  if(A*6 >= B && A <= B){
    printf("Yes");
  }else{
    printf("No");
  }
  return 0;
}
