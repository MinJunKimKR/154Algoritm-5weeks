#include<iostream>
#include<deque>
#define endl "\n"

using namespace std;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	deque<int> silver;

	while (n--) {
		string s;
		cin >> s;

		if (s == "push_front") {
			int temp;
			cin >> temp;
			silver.push_front(temp);
		}
		else if (s == "push_back") {
			int temp;
			cin >> temp;
			silver.push_back(temp);
		}
		else if (s == "pop_front") {
			if (silver.size() > 0) {
				cout << silver.front() << endl;
				silver.pop_front();
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (s == "pop_back") {
			if (silver.size() > 0) {
				cout << silver.back() << endl;
				silver.pop_back();
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (s == "size") {
			cout << silver.size() << endl;
		}
		else if (s == "empty") {
			if (silver.empty()) {
				cout << 1 << endl;
			}
			else
				cout << 0 << endl;
		}
		else if (s == "front") {
			if (silver.size() > 0) {
				cout << silver.front() << endl;
			}
			else {
				cout << -1 << endl;
			}
		}
		else if (s == "back") {
			if (silver.size() > 0) {
				cout << silver.back() << endl;
			}
			else
				cout << -1 << endl;
		}

	}

	return 0;
}