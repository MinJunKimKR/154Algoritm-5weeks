#include<iostream>
#include<algorithm>
#include<queue>
#define endl "\n"

using namespace std;

int DP[1000001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int a;
	cin >> a;

	int count = 0;

	DP[1] = 0;
	DP[2] = 1;
	DP[3] = 1;

	for (int i = 4; i <= a; i++) {
		DP[i] = DP[i - 1] + 1;
		
		if (i % 2 == 0)
			DP[i] = min(DP[i / 2] + 1, DP[i]);
		if (i % 3 == 0)
			DP[i] = min(DP[i / 3] + 1, DP[i]);
	}

	cout << DP[a] << endl;

	return 0;
}