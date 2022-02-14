main(){
  long N,K;
  scanf("%ld %ld",&N,&K);
  for(int i=0;i<K;i++){
    if(N%200==0) N = N/200;
    else N = N*1000+200;
  }
  printf("%ld",N);
}
