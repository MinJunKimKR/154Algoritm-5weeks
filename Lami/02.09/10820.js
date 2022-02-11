const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');
if (input[input.length - 1] === '') input.pop();

function solution() {
  for (let i = 0; i < input.length; i++) {
    const str = input[i];
    const answer = [0, 0, 0, 0];
    const lowCase = str.match(/[a-z]/g);
    const upperCase = str.match(/[A-Z]/g);
    const num = str.match(/[0-9]/g);
    const space = str.match(/[ ]/g);
    if (lowCase) {
      answer[0] = lowCase.length;
    }
    if (upperCase) {
      answer[1] = upperCase.length;
    }
    if (num) {
      answer[2] = num.length;
    }
    if (space) {
      answer[3] = space.length;
    }
    console.log(...answer);
  }
}

solution();
