#include <iostream>
using namespace std;
int main(void){
  int V,S,T,D;
  cin >> V >> T >> S >> D;
  if ( D < T*V || D > S*V ){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }
  return 0;
}
