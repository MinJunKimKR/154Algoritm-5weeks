const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  for (let i = 1; i <= Number(input[0]); i++) {
    let numbers = input[i].split(' ');

    console.log(
      `Case #${i}: ${numbers[0]} + ${numbers[1]} = ${
        Number(numbers[0]) + Number(numbers[1])
      }`
    );
  }
}

solution();
