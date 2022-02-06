#include<iostream>
#include<string>

using namespace std;

int main() {

	string s;
	getline(cin, s);

	for (int i = 0; i < s.length(); i++) {
		if (s[i] >= 'A' and s[i] <= 'z') {
			if (s[i] >= 'a') {
				if (s[i] <= 'm') {
					s[i] += 13;
				}
				else {
					s[i] -= 13;
				}
			}
			else {
				if (s[i] >= 'A') {
					if (s[i] <= 'M') {
						s[i] += 13;
					}
					else {
						s[i] -= 13;
					}
				}
			}
		}
	}

	cout << s << endl;


	return 0;
}