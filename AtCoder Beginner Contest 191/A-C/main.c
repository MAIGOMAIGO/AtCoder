#include <stdio.h>
 
int main(void){
  float V,T,S,D;
  scanf("%f %f %f %f",&V,&T,&S,&D);
  if((D/V < T) || (D/V > S)){
    printf("Yes");
  }else{
    printf("No");
  }
  return 0;
}
