#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int DP[1001];

int main() {

	int n;
	cin >> n;

	vector<int> sequence;
	int temp;

	for (int i = 0; i < n; i++) {
		cin >> temp;
		sequence.push_back(temp);
	}


	//1번을 고를수도 있고 안 고를수도 있음.
	//if(갖고있는것보다 클시)
	//선택 or 안 선택.

	int count = 0;

	for (int i = 1; i < n; i++) {
		for (int j = 0; j < i; j++) {
			if (sequence[i] > sequence[j]) {
				if (DP[i] <= DP[j]) {
					DP[i] = DP[j] + 1;
				}
			}
			else if (sequence[i] < sequence[j]) {
				continue;
			}
			else {
				DP[i] = DP[j];
			}
		}
	}

	cout << *max_element(DP, DP + n) + 1 << endl;

	return 0;
}