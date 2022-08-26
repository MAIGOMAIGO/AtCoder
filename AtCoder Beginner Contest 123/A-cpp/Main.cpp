#include <iostream>
#include <stdlib.h>
using namespace std;
int main(void){
  int a,b,c,d,e,k;
  cin >> a >> b >> c >> d >> e >> k;
  int antenna[5] = {a,b,c,d,e};
  for(int i=0;i < 4;i++){
    for(int j=i+1;j<5;j++){
      if(abs(antenna[i] - antenna[j]) > k){
        cout << ":(";
        return 0;
      }
    }
  }
  cout << "Yay!";
  return 0;
}
