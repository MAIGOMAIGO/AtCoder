## 標準

```javascript
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
});
```

## 標準入力

```javascript
// N 整数
// S 文字列
reader.on('line', (line) => {
  lines.push(line);
});
reader.on('close', () => {
  // 整数
  var N = parseInt(lines[0]);
  // 文字列
  var S = lines[1];
});
```

## 標準出力

```javascript
console.log();
```
