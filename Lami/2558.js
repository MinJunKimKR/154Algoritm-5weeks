/*********************************************************************
 *Title : A+B - 2
 *Number : <img src="https://d2gd6pc034wcta.cloudfront.net/tier/1.svg" class="solvedac-tier">&nbsp;2558번
 *Author : sandoll99
 *Description : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
 *Input : 첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)
 *Output : 첫째 줄에 A+B를 출력한다.
 *Start Time : 2022년 0월 16일 21시 2분 23초
 *End Time : 2022년 0월 16일 시 분 초
 *comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
 *********************************************************************/
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
console.log(+input[0] + +input[1]);
