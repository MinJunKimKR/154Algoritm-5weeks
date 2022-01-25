#include<iostream>
#include<algorithm>

using namespace std;

long long sequence[201][201];

int main() {


	int n;
	cin >> n;

	int k;
	cin >> k;


	int temp = max(n, k);

	for (int i = 1; i <= temp; i++) {
		sequence[0][i] = 1;
	}

	for (int i = 1; i <= temp; i++) {
		sequence[i][1] = 1;
	}

	for (int i = 1; i <= temp; i++) {
		for (int j = 2; j <= temp; j++) {
			sequence[i][j] = (sequence[i][j - 1] + sequence[i - 1][j]) %1000000000;
		}
	}

	cout << sequence[n][k] << endl;

	return 0;
}