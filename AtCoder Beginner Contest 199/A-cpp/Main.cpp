#include <iostream>
int main(void){
  int A,B,C;
  std::cin >> A >> B >> C;
  if(A*A+B*B<C*C){
    std::cout << "Yes";
  }else{
    std::cout << "No";
  }
  return 0;
}
