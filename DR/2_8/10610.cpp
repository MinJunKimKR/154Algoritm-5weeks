#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	// 각 자리수를 내림차순으로 정렬해주기 위해 n을 문자열로 선언
	string n;
	cin >> n;

	sort(n.begin(), n.end(), greater<>());
	
	// 30의 배수가 되어야 하므로 마지막 자리수가 0이어야한다.
	if (n[n.length() - 1] == '0') {
		// n은 최대 10^5개의 숫자로 구성되어 있기에 long long 형으로 각 자리수의 합을 구하는 변수 선언
		long long int digit_sum = 0;
		// 문자열의 각 자리수를 char to int를 통해 더해준다.
		for (auto ch : n) {
			digit_sum += ch - '0';
		}

		// 위에서 구한 자리수의 합이 3으로 나누어지는 경우, 30의 배수가 되는 가장 큰 수 출력
		if (digit_sum % 3 == 0) 
			cout << n;
		// 나누어 떨어지지 않는 경우 30의 배수가 아니므로 -1 출력
		else 
			cout << -1;
	}
	else {
		// 0이 아닌 경우 30의 배수가 아니므로 -1 출력
		cout << -1;
	}
}
