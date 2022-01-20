#include<iostream>

using namespace std;

int twenty_seven[20] = { 31,28,31,30,31,30,31,31,30,31,30,31 };

int sum(int month) {
	int answer = 0;
	for (int i = 0; i < month; i++) {
		answer += twenty_seven[i];
	}
	return answer;
}

int main() {

	int month;
	int day;

	cin >> month >> day;

	
	month--;

	int answer = sum(month) + day;

	string answer_day[7] = { "SUN", "MON" , "TUE" , "WED" , "THU" , "FRI" ,"SAT"};

	//month 전달까지의 모든 날수 더하기 + day 더하고 7로 나눈 나머지 mod 값이 월요일에 더해진다.

	answer %= 7;
	cout << answer_day[answer] << endl;

	return 0;
}