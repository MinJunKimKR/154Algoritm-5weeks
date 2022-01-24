const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  let sum = 0;
  for (let i = 1; i <= Number(input[0]); i++) {
    sum += i;
  }
  console.log(sum);
}

solution();
