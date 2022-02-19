#include <stdio.h>
int main(void){
  unsigned long N;
  scanf("%lu",&N);
  for(int i=sizeof N * 8 -1;i>=0;i--){
    if((N>>i)&1){
      printf("%d",i);
      break;
    }
  }
  return 0;
}
