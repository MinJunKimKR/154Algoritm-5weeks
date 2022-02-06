#include<iostream>

using namespace std;

int fibbonachi[1002];

int main() {

	int a;
	cin >> a;

	fibbonachi[1] = 1;
	fibbonachi[2] = 3;
	fibbonachi[3] = 5;
	fibbonachi[4] = 11;
	fibbonachi[5] = 21;

	for (int i = 5; i <= a; i++) {
		fibbonachi[i] = (fibbonachi[i - 1] + fibbonachi[i - 2]*2)%10007;
	}
	
	cout << fibbonachi[a] << endl;

	return 0;
}