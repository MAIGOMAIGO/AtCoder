#include <stdio.h>

int main(void){
  char str[1000];
  int i;
  scanf("%s",str);
  for(i=0;i<strlen(str);i++){
    if(i%2==0){
      if(str[i]<'a'|| str[i]>'z'){
        printf("No");
        return 0;
      }
    }else{
      if(str[i]<'A'|| str[i]>'Z'){
        printf("No");
        return 0;
      }
    }
  }
  printf("Yes");
  return 0;
}
