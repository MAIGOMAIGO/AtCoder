#include <iostream>
using namespace std;
int main(void){
  int N;
  cin >> N;
  N = N%10;
  if(N==3){
    cout << "bon" << endl;
  }else if(N==0 || N==1 || N==6 || N==8){
    cout << "pon" << endl;
  }else{
    cout << "hon" << endl;
  }
  return 0;
}
