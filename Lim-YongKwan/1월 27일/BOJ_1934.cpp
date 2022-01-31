#include<iostream>
#define endl "\n"
using namespace std;

int gcd(int a, int b) {
	int temp = 0;
	/*
	6	3	0
	3

	21	12	9
	12	9	3
	9	3	0

	10	6	4
	6	4	2
	4	2	0
	2

	*/
	temp = a % b;
	while (temp > 0) {
		a = b;
		b = temp;
		temp = a % b;
	}
	return b;
}

int main() {

	int testcase;
	cin >> testcase;

	while (testcase--) {
		int a;
		int b;
		cin >> a >> b;
		if (b > a)
			swap(a, b);

		cout<<a*b/gcd(a, b)<<endl;
	}

	return 0;
}