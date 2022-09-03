#include <stdio.h>
#define MAX 1000

void x(int n,int h[MAX][3]){
  int i=0;
  for(int j=1;j<n-1;j++){
    for(int k=1;k<n-j;k++){
      h[i][0] = j;
      h[i][1] = k;
      h[i][2] = n-j-k;
      i++;
    }
  }
}

int main(void){
  int h[3],w[3];
  scanf("%d %d %d %d %d %d",&h[0],&h[1],&h[2],&w[0],&w[1],&w[2]);
  int h1[MAX][3]={0},h2[MAX][3]={0},h3[MAX][3]={0};
  x(h[0],h1);x(h[1],h2);x(h[2],h3);
  int c=0;
  for(int i=0;i<MAX;i++){
    if(h1[i][0] == 0)break;
    for(int j=0;j<MAX;j++){
      if(h2[j][0] == 0)break;
      for(int k=0;k<MAX;k++){
        if(h3[k][0] == 0)break;
        if(h1[i][0]+h2[j][0]+h3[k][0]==w[0] && h1[i][1]+h2[j][1]+h3[k][1]==w[1] && h1[i][2]+h2[j][2]+h3[k][2]==w[2])c++;
      }
    }
  }
  printf("%d",c);
  return 0;
}
