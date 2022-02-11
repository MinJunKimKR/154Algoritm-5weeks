const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const line = Number(input[0]);
  let cnt = 1;
  for (let i = 1; i < line; i++) {
    str = '';
    if (i === 1) {
      console.log(' '.repeat(line - i) + '*');
    }
    if (i >= 2) {
      str = '*' + ' '.repeat(cnt) + '*';
      console.log(' '.repeat(line - i) + str);
      cnt += 2;
    }
  }
  console.log('*'.repeat(2 * line - 1));
}

solution();
