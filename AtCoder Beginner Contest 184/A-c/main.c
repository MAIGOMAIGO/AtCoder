main(){
  int N,X;
  scanf("%d %d ",&N,&X);
  for(;N>0;N--){
    char S;
    scanf("%c",&S);
    if(S=='o')X++;
    else if(X>0)X--;
  }
  printf("%d",X);
}
