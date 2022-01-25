#include <stdio.h>
int main(){
  int N;
  scanf("%d",&N);
  if((int)(N * 1.08) < 206){
    printf("Yay!");
  }else if((int)(N * 1.08) == 206){
    printf("so-so");
  }else{
    printf(":(");
  }
  return 0;
}
