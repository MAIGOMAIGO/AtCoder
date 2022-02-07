main(){
  int A,B;
  scanf("%d %d",&A,&B);
  if(A>0 && B==0){
    printf("Gold");
  }else if(A == 0 && B > 0){
    printf("Silver");
  }else{
    printf("Alloy");
  }
}
