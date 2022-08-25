#include <iostream>
using namespace std;

int main(void){
  int N;
  cin >> N;
  int H[N];
  for(int i=0;i<N;i++)cin >> H[i];
  int c=1;
  for(int i=1;i<N;i++){
    int f=1;
    for(int j=0;j<i;j++){
      if(H[j] > H[i]){
        f=0;break;
      }
    }
    if(f)c++;
  }
  cout << c << endl;
  return 0;
}
