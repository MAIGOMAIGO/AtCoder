#include <iostream>

int main(void){
  long long A,B,C=0;
  std::cin >> A >> B;
  while(1){
    if(A != B){
      if(A>B){
        C += A/B;
        A %= B;
      }else{
        C += B/A;
        B %= A;
      }
      if(A==0 || B==0){
        C -= 1;
        break;
      }
    }else{
      break;
    }
  }
  std::cout << C << std::endl;
  return 0;
}
