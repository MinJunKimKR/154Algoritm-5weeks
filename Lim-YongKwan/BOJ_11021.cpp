#include<iostream>

using namespace std;

int main() {

	int testcase;
	cin >> testcase;

	for (int T = 1; T <= testcase; T++) {

		int result;
		int a;
		int b;
		cin >> a >> b;
		result = a + b;

		cout << "Case #" << T << ": "<<a<<" + "<<b<<" = " << result << endl;
	}

	return 0;
}