#include <stdio.h>
 
int main(void){
  int i;
  char s[5];
  (void)scanf("%s",s);
  for(i=0;i<3;i++){
    if((s[i]==s[i+1])&&(s[i+1]==s[i+2])){
      printf("%c",s[i]);
      break;
    }
    if((i+2)==4){
      printf("draw");
    }
  }
