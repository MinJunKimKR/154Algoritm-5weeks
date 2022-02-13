#include<iostream>
#include<algorithm>
#define endl "\n"
using namespace std;

int main() {

	int n;
	cin >> n;

	int total_1 = 0;
	int total_2 = 0;
	int temp = 1;
	for (int i = 2; i <= n; i++) {
		temp = i;

		while (temp % 2 == 0 or temp % 5 == 0) {
			if (temp % 2 == 0) {
				total_1++;
				temp /= 2;
			}
			if (temp % 5 == 0) {
				total_2++;
				temp /= 5;
			}
		}
	}

	cout << min(total_1,total_2) << endl;
	return 0;
}