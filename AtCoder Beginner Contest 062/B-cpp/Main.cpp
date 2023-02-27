#include <iostream>
#include <string>
using namespace std;
int main(void){
  int H,W;
  cin >> H >> W;
  
  for(int i=0;i<W+2;i++)
    cout << "#";
  cout << endl;
  
  string a;
  for(int i=0;i<H;i++){
    cin >> a;
    cout << "#" << a << "#" << endl;
  }
  
  for(int i=0;i<W+2;i++)
    cout << "#";
  cout << endl;
  return 0;
}
