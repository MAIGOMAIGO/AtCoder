#include <stdio.h>
int main(){
  int A,B,C;
  scanf("%d %d %d",&A,&B,&C);
  if(C){
    if(A>=B){
      printf("Takahashi");
    }else{
      printf("Aoki");
    }
  }else{
    if(A>B){
      printf("Takahashi");
    }else{
      printf("Aoki");
    }
  }
  return 0;
}
