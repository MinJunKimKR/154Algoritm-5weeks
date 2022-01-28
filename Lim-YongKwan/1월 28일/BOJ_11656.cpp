#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#define endl "\n"

using namespace std;

int main() {
	
	string s;
	cin >> s;

	string temp;
	vector<string> suffix;
	for (int i = 0; i < s.length(); i++ ) {
		temp = s.substr(i, s.length());
		suffix.push_back(temp);
	}

	sort(suffix.begin(), suffix.end());

	vector<string>::iterator iter;
	
	for (iter = suffix.begin(); iter != suffix.end(); iter++) {
		cout << *iter << endl;
	}

	return 0;
}