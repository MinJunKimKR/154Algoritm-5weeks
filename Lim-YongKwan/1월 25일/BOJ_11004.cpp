#include<iostream>
#include<algorithm>
#include<vector>
#define endl "\n"

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;
	int k;
	cin >> k;

	int temp;
	vector<int> k_number;
	for (int i = 0; i < n;i++) {
		cin >> temp;
		k_number.push_back(temp);
	}

	sort(k_number.begin(), k_number.end());

	cout << k_number[k-1] << endl;

	return 0;
}