#include<iostream>
#include<vector>
#include<algorithm>
#define endl "\n"
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, m;
	cin >> n >> m;
	vector<int> first;
	vector<int> second;
	vector<int>last;
	int temp;

	for (int i = 0; i < n; i++) {
		cin >>temp;
		last.push_back(temp);
	}
	for (int i = 0; i < m; i++) {
		cin >> temp;
		last.push_back(temp);
	}

	sort(last.begin(), last.end());

	for (int i = 0; i < last.size(); i++) {
		cout << last[i] << " ";
	}
	cout << endl;
	return 0;
}