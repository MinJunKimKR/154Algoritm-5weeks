const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const words = input[0];
  const aToZ = 'abcdefghijklmnopqrstuvwxyz';
  let answer = '';
  for (let alphabet of aToZ) {
    let cnt = 0;
    for (let word of words) {
      if (word === alphabet) {
        cnt++;
      }
    }
    answer += String(cnt) + ' ';
  }
  console.log(answer.slice(0, -1));
}

solution();
