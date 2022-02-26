main(){
  int X;scanf("%d",&X);
  if(X>=90){
    printf("expert");
  }else if(X>=70){
    printf("%d",90-X);
  }else if(X>=40){
    printf("%d",70-X);
  }else{
    printf("%d",40-X);
  }
}
