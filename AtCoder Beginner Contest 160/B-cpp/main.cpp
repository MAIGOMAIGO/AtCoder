#include <iostream>
using namespace std;
int main(void){
  unsigned long X;
  cin >> X;
  cout << (X/500)*1000 + (X%500/5)*5 << endl;
  return 0;
}
