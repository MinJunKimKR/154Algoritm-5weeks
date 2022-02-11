const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');
if (input[input.length - 1] === '') input.pop();

function solution() {
  for (let i = 0; i < input.length; i++) {
    let nums = input[i].split(' ');
    console.log(Number(nums[0] + nums[1]) + Number(nums[2] + nums[3]));
  }
}

solution();
