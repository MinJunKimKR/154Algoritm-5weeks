const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const numbers = input[1].split(' ').map((x) => Number(x));
  numbers.sort((a, b) => a - b);
  console.log(`${numbers[0]} ${numbers[Number(input[0]) - 1]}`);
}

solution();
