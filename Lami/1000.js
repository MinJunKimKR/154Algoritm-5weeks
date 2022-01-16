/*********************************************************************
 *Title : A+B
 *Number : <img src="https://d2gd6pc034wcta.cloudfront.net/tier/1.svg" class="solvedac-tier">&nbsp;1000번
 *Author : sandoll99
 *Description : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
 *Input : 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
 *Output : 첫째 줄에 A+B를 출력한다.
 *Start Time : 2022년 0월 16일 20시 50분 55초
 *End Time : 2022년 0월 16일 시 분 초
 *comments program : https://chrome.google.com/webstore/detail/boj-blog-post/ehhcjhfkaiohgflkjifmageahncijacd?hl=ko
 *********************************************************************/
let input = require('fs').readFileSync('/dev/stdin').toString().split(' ');
let a = parseInt(input[0]);
let b = parseInt(input[1]);

console.log(a + b); // 3
