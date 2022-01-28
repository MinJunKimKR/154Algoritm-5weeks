const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const whiteSpace = ' ';
  const star = '*';
  let answer = '';
  for (let i = 1; i <= Number(input[0]); i++) {
    answer = whiteSpace.repeat(Number(input[0]) - i) + star.repeat(i);
    console.log(answer);
  }
}

solution();
