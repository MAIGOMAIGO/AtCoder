process.stdin.resume();
process.stdin.setEncoding('utf8');

var lines = [];
var reader = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
reader.on('line', (line) => {
  lines.push(line);
});
reader.on('close', () => {
  var N = parseInt(lines[0]);
  var S = lines[1];
  if(S.indexOf('1',0)%2){
    console.log('Aoki');
  }else{
    console.log('Takahashi');
  }
});
