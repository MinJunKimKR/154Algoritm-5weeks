const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  for (let i = 1; i <= 9; i++) {
    console.log(`${input[0]} * ${i} = ${input[0] * i}`);
  }
}

solution();
