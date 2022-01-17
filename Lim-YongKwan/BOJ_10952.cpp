#include<iostream>

using namespace std;

int main() {

	int a;
	int b;
	while (cin >> a && cin >> b) {
		if (a == 0 && b == 0)
			break;
		cout << a + b << endl;
	}

	return 0;
}