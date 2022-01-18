#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#define endl "\n"

using namespace std;

int split(string input, char delimeter);

int main() {

	int testcase;
	cin >> testcase;
	while (testcase--) {

		string s;
		cin >> s;

		int answer = 0;

		answer = split(s, ',');

		cout << answer << endl;
	}

	return 0;
}

int split(string input, char delimeter) {
	vector<int> answer;
	stringstream ss(input);
	string temp;

	int result = 0;

	while (getline(ss, temp, delimeter)) {
		answer.push_back(stoi(temp));
		result += stoi(temp);
	}

	return result;
}