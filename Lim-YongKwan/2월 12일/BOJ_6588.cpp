#include<iostream>
#define endl "\n"
using namespace std;

int prime[1000001];

void eratos() {
	prime[1] = 1;
	for (int i = 3; i <= 1000; i++) {
		if(prime[i] == 0){
			for (int j = i*i; j <= 1000000; j += i) {
				prime[j] = 1;
			}
		}
	}
	return;
}

void eratos_visit(int n) {
	
	if (n > 2) {
		if (n % 2 == 1) {
			cout << "Goldbach's conjecture is wrong." << endl;
			return;
		}
	}

	for (int i = 3; i <= n; i += 2) {
		if (prime[i] == 0) {
			if (prime[n - i] == 0) {
				cout << n << " = " << i << " + " << n - i << endl;
				return;
			}
		}
	}

	cout << "Goldbach's conjecture is wrong." << endl;
	return;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL);
	int n = 0;
	eratos();

	while (true) {
		cin >> n;
		if (n == 0) {
			break;
		}
		eratos_visit(n);
	}


	return 0;
}