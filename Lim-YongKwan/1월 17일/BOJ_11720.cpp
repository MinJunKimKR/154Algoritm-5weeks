#include<iostream>
#include<string>
using namespace std;

int main() {

	int n;
	cin >> n;
	char s;
	int total = 0;
	for (int i = 0; i < n; i++) {
		cin >> s;
		total += (int)s - 48;
	}
	cout << total << endl;
	return 0;
}