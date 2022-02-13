#include<iostream>
#include<string>
#include<vector>
#include<math.h>
#define endl "\n"

using namespace std;

int main() {

	string s;
	cin >> s;
	string answer = "";
	int temp = 0;
	int num = 0;

	if (s == "0") {
		cout << 0 << endl;
		return 0;
	}

	if (s.length() > 333334) {
		cout << 0 << endl;
		return 0;
	}

	for(int i = s.length()-1; i >= 0; i--) {

		temp = s[i] - '0';
	//	cout << "temp : " << temp << endl;
		
		if (i != 0) {
			for (int j = 0; j < 3; j++) {
				num = temp % 2;
				answer += to_string(num);
			//	cout << "answer : " << answer << endl;
				temp /= 2;
			}
		}
		num = 0;
		if (i == 0) {
			while (temp > 0) {
				num = temp % 2;
				answer += to_string(num);
				temp /= 2;
			}
		}
	}

	for (int i = answer.length()-1; i >=0; i--) {
		cout << answer[i];
	}
	return 0;
}