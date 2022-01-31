const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  for (let i = Number(input[0]); i > 0; i--) {
    console.log('*'.repeat(i));
  }
}

solution();
