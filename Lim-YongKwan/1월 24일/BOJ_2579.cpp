#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {

	int n;
	cin >> n;

	int temp;

	vector<int> stair;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		stair.push_back(temp);
	}

	int DP[301];
	DP[0] = stair[0];
	DP[1] = stair[0] + stair[1];


	for (int i = 2; i < n; i++) {
		DP[i] = max(stair[i - 1] + DP[i - 3] +stair[i], DP[i-2] +stair[i]);
	}

	cout << DP[n-1] << endl;

	return 0;
}