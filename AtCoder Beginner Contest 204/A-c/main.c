main(){
  int x,y,i;
  scanf("%d %d",&x,&y);
  if(x == y){
    printf("%d",x);
  }else{
    for(i=0;i<3;i++){
      if(x!=i&&y!=i){
        printf("%d",i);
        break;
      }
    }
  }
}
