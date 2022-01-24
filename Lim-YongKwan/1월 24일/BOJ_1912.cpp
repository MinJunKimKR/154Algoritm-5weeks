#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main() {

	int n;
	cin >> n;
	int temp;
	vector<int> sequence;

	for (int i = 0; i < n; i++) {
		cin >> temp;
		sequence.push_back(temp);
	}

	vector<int> DP;
	DP.push_back(sequence[0]);

	for (int i = 1; i < n; i++) {
		DP.push_back(sequence[i]);
		if (DP[i - 1] > 0)
			DP[i] += DP[i - 1];
	}

	cout << *max_element(DP.begin(), DP.end()) << endl;

	return 0;
}