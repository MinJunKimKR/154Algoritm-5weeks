const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  for (let i = 0; i < 10; i++) {
    console.log(input[0].substr(i * 10, 10));
  }
}

solution();
