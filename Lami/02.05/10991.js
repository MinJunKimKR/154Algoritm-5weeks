const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const line = Number(input[0]);
  for (let i = 1; i <= line; i++) {
    let str = '';
    for (let j = 1; j <= 2 * i - 1; j++) {
      if (j % 2) {
        str += '*';
      } else {
        str += ' ';
      }
    }
    console.log(' '.repeat(line - i) + str);
  }
}

solution();
