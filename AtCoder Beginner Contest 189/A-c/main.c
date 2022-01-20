main(){
  char C[3];
  scanf("%s%s%s",&C[0],&C[1],&C[2]);
  if((C[0]==C[1])&&(C[1]==C[2]))printf("Won");
  else printf("Lost");
}
