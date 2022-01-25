#include<iostream>
#include<vector>
#include<algorithm>
#define endl "\n"

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

	DP.push_back(1);

	for (int i = 1; i < n; i++) {
		DP.push_back(1);
		for (int j = 0; j < i; j++) {
			if (sequence[i] < sequence[j]) {
				if(DP[i]<=DP[j])
					DP[i] = DP[j] + 1;
			}
		}
	}

	cout << *max_element(DP.begin(), DP.end()) << endl;

	return 0;
}