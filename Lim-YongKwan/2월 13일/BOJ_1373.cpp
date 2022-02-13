#include<iostream>
#include<string>
#include<vector>
#include<math.h>
#define endl "\n"
using namespace std;


int main() {

	string s;
	cin >> s;
	
	vector<int> last;
	int temp = 0;
	int hexa = 0;

	for (int i = s.length()-1; i >=0; i--) {

		hexa += (s[i]-'0') * pow(2,temp);
		//cout << "hexa : " << hexa << endl;
		temp++;
		if (temp == 3) {
			temp = 0;
			last.push_back(hexa);
			hexa = 0;
		}
	}
	if (temp != 0) {
		last.push_back(hexa);
	}

	for (int i = last.size()-1; i >=0; i--) {
		cout << last[i];
	}

	return 0;
}