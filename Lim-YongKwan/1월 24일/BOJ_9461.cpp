#include<iostream>

using namespace std;

long long tide[101];

int main() {

	int testcase;
	cin >> testcase;

	while (testcase--) {

		int n;
		cin >> n;

		tide[0] = 1;
		tide[1] = 1;
		tide[2] = 1;
		tide[3] = 2;
		tide[4] = 2;

		for (int i = 5; i < n; i++) {
			tide[i] = tide[i - 2] + tide[i - 3];
		}

		cout << tide[n-1] << endl;

	}

	return 0;
}