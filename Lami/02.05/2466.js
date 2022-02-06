const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const line = Number(input[0]);
  for (let i = 0; i < line; i++) {
    console.log(' '.repeat(i) + '*'.repeat(2 * line - 1 - 2 * i));
  }
  for (let i = line - 2; i >= 0; i--) {
    console.log(' '.repeat(i) + '*'.repeat(2 * line - 1 - 2 * i));
  }
}

solution();
