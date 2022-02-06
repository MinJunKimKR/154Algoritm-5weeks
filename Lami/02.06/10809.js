const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const words = input[0];
  const aToZ = 'abcdefghijklmnopqrstuvwxyz';
  let answer = '';
  for (let alphabet of aToZ) {
    let result = words.indexOf(alphabet);
    answer += String(result) + ' ';
  }
  console.log(answer.slice(0, -1));
}

solution();
