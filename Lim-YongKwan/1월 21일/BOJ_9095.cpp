#include<iostream>
#define endl "\n"

using namespace std;

int fibbonachi[12];

int main() {

	int testcase;
	cin >> testcase;

	fibbonachi[1] = 1;
	fibbonachi[2] = 2;
	fibbonachi[3] = 4;

	while (testcase--) {

		int a;
		cin >> a;

		for (int i = 4; i <= a; i++) {
			fibbonachi[i] = fibbonachi[i - 1] + fibbonachi[i - 2] + fibbonachi[i - 3];
		}
		cout << fibbonachi[a] << endl;
	}

	return 0;
}