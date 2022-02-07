#include <stdio.h>
int main(void){
  char X[4];
  scanf("%s",X);
  if((X[0]==X[1]) && (X[1]==X[2]) && (X[2]==X[3])){
    printf("Weak");
    return 0;
  }
  for(int i=0;i<3;i++){
    if((X[i]!='9')||(X[i+1]!='0')){
      if(X[i]+1!=X[i+1]){
        printf("Strong");
        return 0;
      }
    }
  }
  printf("Weak");
  return 0;
}
