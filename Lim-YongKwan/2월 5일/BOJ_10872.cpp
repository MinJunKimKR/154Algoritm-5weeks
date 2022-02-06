#include<iostream>

using namespace std;

int main() {

	long long factorial = 1;
	int a;
	cin >> a;

	while (a>0) {
		factorial *= a;
		a--;
	}
	cout << factorial << endl;

	return 0;
}