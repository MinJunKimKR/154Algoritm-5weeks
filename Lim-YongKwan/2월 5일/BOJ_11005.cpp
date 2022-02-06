#include<iostream>
#include<string>

using namespace std;

void decimal(int a, int b) {

	string s = "";
	
	int mod = 0;

	while (a>0) {

		mod = a % b;
		a /= b;
		
		if (mod < 10) {
			s += to_string(mod);
		}
		else {
			char temp = mod + 55;
			s += temp;
		}
		mod = a % b;
	}


	for (int i = s.length()-1; i>=0; i--) {
		cout << s[i];
	}

	return;
}

int main() {

	int n;
	int b;
	cin >> n >> b;

	decimal(n, b);

	return 0;
}