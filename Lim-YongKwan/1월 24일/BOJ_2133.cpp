#include<iostream>
#include<math.h>

using namespace std;

long long DP[2][31];

int main() {

	int n;
	cin >> n;
	DP[0][0] = 1;
	DP[1][0] = 1;
	DP[0][2] = 3;
	DP[1][2] = 3; //새로 늘어난 숫자.
	DP[0][4] = 11;
	DP[1][4] = 2; //새로 늘어난 중복이 없는 특별한 숫자.
	
	for (int i = 6; i <= n; i+=2) {
		DP[1][i] = 2;
		for (int j = 2; j < i; j += 2) {
			DP[0][i] += DP[0][i - j] * DP[1][j];
		}
		DP[0][i] += 2;
	}

	cout << DP[0][n] << endl;

	return 0;
}