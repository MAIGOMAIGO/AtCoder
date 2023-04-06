#include <iostream>

int main(void){
  int X,Y;
  std::cin >> X >> Y;
  int money = 0;
  money += X==1?300000:X==2?200000:X==3?100000:0;
  money += Y==1?300000:Y==2?200000:Y==3?100000:0;
  money += money==600000?400000:0;
  std::cout << money << std::endl;
  return 0;
}
