#include<iostream>
#include<string>
#include<math.h>

using namespace std;

void decimal(string s, int b) {

	long long a = 0;
	
	int temp = 0;
	for (int i = s.length()-1; i >=0; i--) {
		
		if (s[i] >= 'A') {
			a = a+((s[i] - 55)) * pow(b,temp);
		}
		else {
			
			a += ((s[i]-48) * pow(b,temp));
		}
		temp++;
	}

	cout << a << endl;
}

int main() {

	string s;
	int b;
	cin >> s >> b;
	decimal(s, b);

	return 0;
}