#include<iostream>
#include<algorithm>
#define endl "\n"

using namespace std;

void combination_end(int n, int m) {

	int two_num = 0;
	int five_num = 0;

	int temp = n - m;
	

	for (long long i = 5; i <= n; i *= 5) {
		five_num += n / i;
	}
	for (long long i = 2; i <= n; i *= 2) {
		two_num += n / i;
	}
	for (long long i = 5; i <= m; i *= 5) {
		five_num -= m / i;
	}
	for (long long i = 2; i <= m; i *= 2) {
		two_num -= m / i;
	}
	for (long long i = 5; i <= temp; i *= 5) {
		five_num -= temp / i;
	}
	for (long long i = 2; i <= temp; i *= 2) {
		two_num -= temp / i;
	}


	cout << min(two_num, five_num) << endl;
	return;
}

int main() {

	int n, m;
	cin >> n >> m;

	combination_end(n, m);

	return 0;
}