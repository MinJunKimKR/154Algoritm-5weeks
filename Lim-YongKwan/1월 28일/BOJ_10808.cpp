#include<iostream>
#include<string>

using namespace std;

int main() {

	int alphabet[27] = { 0, };

	string s;
	getline(cin, s);
	int temp = 0;
	for (int i = 0; i < s.size();i++) {
		temp = s[i] - 'a';
		alphabet[temp]++;
	}

	for (int i = 0; i < 26; i++) {
		if(i<25)
			cout << alphabet[i] << " ";
		else {
			cout << alphabet[i];
		}
	}

	return 0;
}