#include<iostream>
#include<string>
#define endl "\n"
using namespace std;

int main() {

	string s;
	while (getline(cin, s)) {

		int small_letter = 0;
		int capital = 0;
		int space = 0;
		int number = 0;

		for (int i = 0; i < s.length(); i++) {
			if (s[i] == ' ') {
				space++;
			}
			else if (s[i] >= 'a' && s[i] <= 'z') {
					small_letter++;
				}
				else if (s[i] >= 'A' && s[i] <= 'Z') {
					capital++;
				}
				else
					number++;
			}

			cout << small_letter << " " << capital << " " << number << " " << space << endl;
		}
	
	return 0;
}