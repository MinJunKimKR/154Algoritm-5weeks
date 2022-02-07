const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const line = Number(input[0]);
  for (let i = 1; i <= line; i++) {
    console.log('*'.repeat(i) + ' '.repeat((line - i) * 2) + '*'.repeat(i));
  }
  for (let i = 1; i <= line - 1; i++) {
    console.log(
      '*'.repeat(line - i) + ' '.repeat(i * 2) + '*'.repeat(line - i)
    );
  }
}

solution();
