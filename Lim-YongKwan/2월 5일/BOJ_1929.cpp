#include<iostream>
#define endl "\n"
using namespace std;

int prime[1000001];

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int first;
	int second;
	cin >> first >> second;
	prime[1] = -1;

	for (int i = 2; i*i <= second; i++) {
		if (prime[i] == -1)
			continue;
		else {
			for (int j = i; j*i <= second; j++) {
				prime[j*i] = -1;
			}
		}
	}

	for (int i = first; i <= second; i++) {
		if (prime[i] == 0) {
			cout << i << endl;
		}
	}

	return 0;
}