#include <iostream>
using namespace std;
int main(void){
  int N,S,D;
  cin >> N >> S >> D;
  int X[N],Y[N];
  for(int i=0;i<N;i++){
    cin >> X[i] >> Y[i];
    if(X[i] < S && D < Y[i]){
      printf("Yes");
      return 0;
    }
  }
  printf("No");
  return 0;
}
