#include<iostream>
#include<algorithm>

using namespace std;

int main() {

	int n, m, k;
	cin >> n >> m >> k;
	
	int answer = 0;
	while (n + m >= k and n>=0 and m>=0) {
		n -= 2;
		m--;
		answer++;
	}
	cout << answer-1 << endl;

	return 0;
}