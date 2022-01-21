const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  let answer = '';
  for (let i = Number(input[0]); i >= 1; i--) {
    if (i === 1) {
      answer += i;
    } else {
      answer += `${i}\n`;
    }
  }
  console.log(answer);
}

solution();
