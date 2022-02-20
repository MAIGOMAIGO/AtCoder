main(){
  char S[3];
  scanf("%s",&S);
  if(S[0]==S[1] && S[1]==S[2]){
    printf("%d",S[0]=='R'?3:0);
  }else if(S[0]==S[1] || S[1]==S[2]){
    printf("%d",S[1]=='S'?1:2);
  }else{
    printf("1");
  }
}
