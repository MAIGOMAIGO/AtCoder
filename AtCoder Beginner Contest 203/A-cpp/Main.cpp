#include <iostream>
using namespace std;
int main(void){
  int a,b,c;
  cin >> a >> b >> c;
  if(a==b){
    cout << c << endl;
  }else if(b==c){
    cout << a << endl;
  }else if(a==c){
    cout << b << endl;
  }else{
    cout << 0 << endl;
  }
  return 0;
}
