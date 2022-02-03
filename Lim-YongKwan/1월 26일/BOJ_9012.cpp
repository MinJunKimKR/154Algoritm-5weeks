#include<iostream>
#include<stack>
#include<string>
#define endl "\n"

using namespace std;

int main() {

	int n;
	cin >> n;

	while (n--) {
		stack<char> bracket;

		string s;
		cin >> s;
		bracket.push(s[0]);

		for (int i = 1; i < s.length(); i++) {
			if (bracket.size() != 0 && s[i] != bracket.top() && s[i] == ')') {
				bracket.pop();
			}
			else {
				bracket.push(s[i]);
			}
		}

		if (bracket.size() != 0) {
			cout << "NO" << endl;
		}
		else {
			cout << "YES" << endl;
		}
		bracket.empty();

	}
	return 0;
}