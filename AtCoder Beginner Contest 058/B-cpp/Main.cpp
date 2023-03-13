#include <iostream>
#include <string>
using namespace std;
int main(void){
  string O,E;
  cin >> O >> E;
  for(int i=0;i<E.length();i++){
    cout << O[i] << E[i];
  }
  if(O.length()>E.length())
    cout << O[O.length()-1];
  cout << endl;
  return 0;
}
