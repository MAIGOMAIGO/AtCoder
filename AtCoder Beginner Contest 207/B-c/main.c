#include <stdio.h>
int main(){
  long A,B,C,D;
  scanf("%ld %ld %ld %ld",&A,&B,&C,&D);
  long blue = A,red = 0;
  for(int i = 1;i <= A;i++){
    blue += B;
    red += C;
    if(blue <= D*red){
      printf("%ld",i);
      return 0;
    }
  }
  printf("%d",-1);
  return 0;
}
