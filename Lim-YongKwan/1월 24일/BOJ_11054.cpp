#include<iostream>
#include<vector>

#define endl "\n"

using namespace std;

int main() {

	int n;
	cin >> n;
	int temp;
	vector<int> sequence;

	for (int i = 0; i < n; i++) {
		cin >> temp;
		sequence.push_back(temp);
	}
	
	int DP[2][1001];

	DP[0][0] = 1;

	for (int i = 1; i < n; i++) {
		DP[0][i] = 1;
		for (int j = 0; j < i; j++) {
			if (sequence[i] > sequence[j]) {
				if (DP[0][i] <= DP[0][j]) {
					DP[0][i] = DP[0][j] + 1;
				}
			}
		}
	}

	DP[1][n - 1] = 1;

	for (int i = n - 1; i >= 0; i--) {
		DP[1][i] = 1;
		for (int j = n - 1; j > i; j--) {
			if (sequence[i] > sequence[j]) {
				if (DP[1][i] <= DP[1][j]) {
					DP[1][i] = DP[1][j] + 1;
				}
			}
		}
	}

	int max = 0;

	for (int i = 0; i < n; i++) {
		if (DP[0][i] + DP[1][i] > max)
			max = DP[0][i] + DP[1][i];
	}

	/*for (int i = 0; i < n; i++) {
		cout << "DP : " << DP[0][i] + DP[1][i] << " ";
	}
	cout << endl;
	*/
	cout << max-1 << endl;

	return 0;
}