const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().split('\n');

function solution() {
  const month = Number(input[0].split(' ')[0]);
  const day = Number(input[0].split(' ')[1]);
  const days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'];
  const monthToDays = {
    28: [2],
    30: [4, 6, 9, 11],
    31: [1, 3, 5, 7, 8, 10, 12],
  };
  let sum = 0;

  for (let i = 1; i < month; i++) {
    for (let m in monthToDays) {
      if (monthToDays[m].includes(i)) {
        sum += Number(m);
      }
    }
  }
  sum += day - 1;
  console.log(days[sum % 7]);
}

solution();
