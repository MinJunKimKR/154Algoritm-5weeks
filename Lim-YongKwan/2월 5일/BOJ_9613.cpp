#include<iostream>
#include<vector>

using namespace std;

int gcd_sum(int a, int b) {

	if (b > a) {
		swap(a, b);
	}
	int temp = 0;

	while (b > 0) {
		temp = a % b;
		a = b;
		b = temp;
	}

	return a;
}

int main() {

	int testcase;
	cin >> testcase;
	while (testcase--) {
		int n;
		cin >> n;

		vector<int> gcd;
		int temp;

		for (int i = 0; i < n; i++) {
			cin >> temp;
			gcd.push_back(temp);
		}

		long long total = 0;
		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {
				total += gcd_sum(gcd[i], gcd[j]);
			}
		}
		cout << total << endl;
	}

	return 0;
}