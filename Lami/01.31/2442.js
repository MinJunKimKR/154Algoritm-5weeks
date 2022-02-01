const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const line = Number(input[0]);
  for (let i = 1; i <= 2 * line - 1; i += 2) {
    console.log(' '.repeat((2 * line - 1 - i) / 2) + '*'.repeat(i));
  }
}

solution();
