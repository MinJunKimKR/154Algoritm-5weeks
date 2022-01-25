#include<iostream>
#include<vector>
#include<string>

using namespace std;

long long code[5001];
long long dp[5001];

int main() {

	string source;
	getline(cin, source);

	if (source.length() > 5000)
		exit(-1);

	if (source[0]-'0' == 0) {
		cout << "0" << endl;
	}
	else {
		for (int i = 0; i < source.length(); i++)
			code[i + 1] = source[i] - '0';

		dp[0] = 1;

		int temp;

		for (int i = 1; i <= source.length(); i++) {

			if (code[i] >= 1 and code[i] <= 9)
				dp[i] += dp[i - 1] % 1000000;

			temp = (code[i - 1]) * 10 + (code[i]);

			if (temp >= 10 and temp <= 26) {
				dp[i] = (dp[i]+ dp[i - 2]) % 1000000;
			}
		}

		cout << dp[source.length()] << endl;
	}
	return 0;
}