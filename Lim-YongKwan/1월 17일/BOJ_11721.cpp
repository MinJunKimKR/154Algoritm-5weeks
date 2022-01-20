#include<iostream>
#define endl "\n"
using namespace std;

int main() {

	string s;
	cin >> s;
	for (int i = 0; i < s.length(); i++) {
		if (i>0 && i % 10 == 0) {
			cout << endl;
		}
		cout << s[i];
	}

	return 0;
}