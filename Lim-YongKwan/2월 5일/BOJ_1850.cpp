#include<iostream>
#define endl "\n"

using namespace std;

long long gcd(long long a, long long b) {
	long long temp = 0;

	
	/*
	16 12 4
	12 4 0
	4 0 
	*/

	while (b > 0) {
		temp = a % b;
		a = b;
		b = temp;
	}

	return a;
}

int main() {

	long long a, b;
	cin >> a >> b;
	if (b > a)
		swap(a, b);

	long long answer = gcd(a, b);

	for (int i = 0; i < answer; i++) {
		cout << "1";
	}
	
	return 0;
}