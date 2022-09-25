#include <stdio.h>
int main(void){
  int K;scanf("%d",&K);
  if(K >= 60){
    printf("22:%02d",K-60);
  }else{
    printf("21:%02d",K);
  }
  return 0;
}
