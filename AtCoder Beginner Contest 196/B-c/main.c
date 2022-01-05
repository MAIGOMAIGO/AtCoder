#include <stdio.h>
#include <string.h>
int main(void){
  int i;
  char x[256];
  scanf("%s",x);
  for(i=0;i<strlen(x);i++){
    if(x[i]=='.')break;
    printf("%c",x[i]);
  }
  return 0;
}
