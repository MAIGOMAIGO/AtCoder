#include<stdio.h>
int main(void){
  int N;scanf("%d",&N);
  switch(N%10){
    case 3:
      printf("bon");
      break;
    case 0:
    case 1:
    case 6:
    case 8:
      printf("pon");
      break;
    default:
      printf("hon");
  }
  return 0;
}
