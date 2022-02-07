#include<iostream>
#define endl "\n"
using namespace std;

int main() {

	int n;
	cin >> n;

	int prime[1001] = { 0, };

	prime[1] = -1;

	for (int i = 2; i*i <= 1000; i++) {
		if (prime[i] == 0) {
			for (int j = i; j * i <= 1000; j++) {
				prime[j * i] = -1;
			}
		}
		
	}

	int prime_num = 0;
	int answer = 0;
	for (int i = 0; i < n; i++) {
		cin >> prime_num;
		if (prime[prime_num] == 0) {
			answer++;
		}
	}

	cout << answer << endl;
	return 0;
}