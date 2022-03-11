main(){
  int A,B,C;
  scanf("%d %d %d",&A,&B,&C);
  if(A > B && C > B){
    printf("%d",A+C);
  }else if(A > C && B > C){
    printf("%d",A+B);
  }else{
    printf("%d",B+C);
  }
}
