main(){
  int A,B;
  scanf("%d %d",&A,&B);
  int a = (A/100)%10+(A/10)%10+A%10;
  int b = (B/100)%10+(B/10)%10+B%10;
  printf("%d",a>b?a:b);
}
