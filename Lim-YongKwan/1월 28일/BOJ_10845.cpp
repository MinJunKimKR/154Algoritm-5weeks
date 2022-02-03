#include<iostream>
#include<queue>
#include<string>
#define endl "\n"
using namespace std;

int main() {

	int n;
	cin >> n;

	queue<int> silver;
	while (n--) {


		string s;
		cin >> s;
		int temp;

		if (s == "push") {
			cin >> temp;
			silver.push(temp);
		}
		else if (s == "front") {
			if (silver.size() > 0) {
				cout << silver.front() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (s == "pop") {
			if (silver.size() > 0) {
				cout << silver.front() << endl;
				silver.pop();
			}
			else {
				cout << "-1" << endl;
			}
		}
		else if (s == "size") {
			cout << silver.size() << endl;
		}
		else if (s == "empty") {
			if (silver.empty()) {
				cout << 1 << endl;
			}
			else {
				cout << 0 << endl;
			}
		}
		else if (s == "back") {
			if (silver.size() > 0) {
				cout << silver.back() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
		
	}
	return 0;
}