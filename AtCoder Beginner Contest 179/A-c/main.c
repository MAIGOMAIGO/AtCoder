#include <stdio.h>
#include <string.h>
int main(void){
  char str[1000];
  scanf("%s",str);
  printf("%s%s",str,str[strlen(str)-1]=='s'?"es":"s");
  return 0;
}
