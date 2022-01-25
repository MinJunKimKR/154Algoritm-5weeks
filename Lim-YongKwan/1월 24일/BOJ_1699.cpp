#include<iostream>
#include<math.h>
#include<algorithm>
using namespace std;

long long square[100001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n;
	cin >> n;

	square[0] = 0;
	square[1] = 1;
	square[2] = 2;
	square[3] = 3;

	for (int i = 1; i <= n; i++) {
		square[i] = i;
		for (int j = 1; j * j <= i; j++) {
			square[i] = min(square[i], square[i - j * j] + 1);
		}
	}

	cout << square[n] << endl;

	return 0;
}