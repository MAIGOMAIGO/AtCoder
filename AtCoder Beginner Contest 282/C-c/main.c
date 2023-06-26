#include <stdio.h>
int main(void){
  int N;
  scanf("%d\n",&N);
  char c;
  int f = 1;
  int i;
  for(i = 0;i<N;i++){
    scanf("%c",&c);
    if(c == '"'){
      f = ~f;
    }
    if(c == ',' && f == 1){
      printf("%c",'.');
    }else{
      printf("%c",c);
    }
  }
  printf("\n");
  return 0;
}
