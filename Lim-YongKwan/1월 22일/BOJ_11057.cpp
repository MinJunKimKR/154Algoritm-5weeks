#include<iostream>

using namespace std;

int DP[1001][10];

int main() {

	int n;
	cin >> n;
	
	for (int i = 0; i <= 9; i++) {
		DP[1][i] = 1;
	}
	for (int i = 1; i <= n; i++) {

		for (int j = 0; j <= 9; j++) {
			for (int k = j; k <= 9; k++) {
				DP[i][j] += (DP[i - 1][k])%10007;
			}
		}
	}

	long long answer =.0;
	for (int i = 0; i <= 9; i++) {
		answer += DP[n][i];
	}


	cout << answer % 10007 << endl;

	return 0;
}