#include <iostream>
using namespace std;
int main(void){
  int N,M;
  cin >> N >> M;
  int A[M],B[M];
  for(int i=0;i<M;i++){
    cin >> A[i] >> B[i];
  }
  int K;
  cin >> K;
  int C[K],D[K];
  for(int i=0;i<K;i++){
    cin >> C[i] >> D[i];
  }
  int top=0;
  for(int i=0;i<pow(2,K);i++){
    int l=i;
    int tes[K];
    for(int z=K;z>0;z--){
      if(l >= pow(2,z-1)){
        tes[K-z]=D[K-z];
        l = l - pow(2,z-1);
      }
      else{
        tes[K-z]=C[K-z];
      }
    }
    int po=0;
    for(int z=0;z<M;z++){
      int fla=0,flb=0;
      for(int l=0;l<K;l++){
        if(A[z]==tes[l])fla=1;
        if(B[z]==tes[l])flb=1;
        if((fla==1)&&(flb==1)){
          po++;
          break;
        }
      }
    }
    if(po > top)top = po;
  }
  cout << top;
  return 0;
}
