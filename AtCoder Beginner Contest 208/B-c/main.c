#include <stdio.h>
int main(){
  int G[11] = {1};
  for(int i=1;i<=10;i++){
    G[i] = G[i-1]*i;
  }
  int P,X=0;
  scanf("%d",&P);
  while(P > 0){
    for(int i=10;i>=1;i--){
      if(G[i] <= P){
        P-=G[i];
        X++;
        break;
      }
    }
  }
  printf("%d",X);
  return 0;
}
