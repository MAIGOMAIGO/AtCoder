#include <stdio.h>
#include <math.h>
int main(void){
  int N;scanf("%d",&N);
  int A[N][N];
  for(int i=0;i<N;i++){
    char s[N];scanf("%s",s);
    for(int j=0;j<N;j++){
      A[i][j] = (int)s[j]-48;
    }
  }
  int P[N],x,y;
  long long m = 0;
  for(int i=0;i<N;i++){
    for(int j=0;j<N;j++){
      for(int v=0;v<8;v++){
        if(v==0){
          x=1;y=0;
        }else if(v==1){
          x=1;y=1;
        }else if(v==2){
          x=0;y=1;
        }else if(v==3){
          x=-1;y=1;
        }else if(v==4){
          x=-1;y=0;
        }else if(v==5){
          x=-1;y=-1;
        }else if(v==6){
          x=0;y=-1;
        }else if(v==7){
          x=1;y=-1;
        }
        int p[N];p[0] = A[i][j];
        int xi=j,yi=i;
        long long M = 0;
        for(int k=1;k<N;k++){
          xi += x;yi += y;
          if(xi < 0)xi += N;
          else if(xi >= N)xi -= N;
          if(yi < 0)yi += N;
          else if(yi >= N)yi -= N;
          p[k] = A[yi][xi];
        }
        for(int l=N-1;l>=0;l--){
          M += p[N-l-1]*pow(10,l);
        }
        if(m < M){
          for(int z=0;z<N;z++){
            P[z] = p[z];
          }
          m = M;
        }
      }
    }
  }
  for(int i=0;i<N;i++){
    printf("%d",P[i]);
  }
  return 0;
}
