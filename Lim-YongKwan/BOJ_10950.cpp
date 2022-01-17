#include<iostream>
#define endl "\n"
using namespace std;

int main() {
	int n;
	cin >> n;
	int a = 0;
	int b=0;

	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		cout << a + b << endl;
	}

	return 0;
}