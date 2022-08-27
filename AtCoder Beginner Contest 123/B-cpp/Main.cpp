#include <iostream>
using namespace std;
int main(void){
  int A,B,C,D,E;
  cin >> A >> B >> C >> D >> E;
  int menu[5] = {A,B,C,D,E}; 
  int m=0,min = 10;
  for(int i=0;i<5;i++){
    if(min>menu[i]%10 && menu[i]%10 != 0){
      min = menu[i]%10;
      m = i;
    }
  }
  int sum=0;
  for(int i=0;i<5;i++){
    if(i == m){
      sum += menu[i];
    }else{
      sum += (menu[i]/10)*10+(menu[i]%10>0?10:0);
    }
  }
  cout << sum;
  return 0;
}
