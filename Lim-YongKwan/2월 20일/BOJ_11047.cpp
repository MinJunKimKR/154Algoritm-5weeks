#include<iostream>
#include<vector>

using namespace std;

int main() {

	int n;
	cin >> n;
	int coin;
	cin >> coin;
	int temp = 0;
	vector<int> coin_num;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		coin_num.push_back(temp);
	}
	temp = 0;
	for(int i = coin_num.size() - 1; i >= 0; i--) {
		if (coin_num[i] > coin)
			continue;
		temp += coin / coin_num[i];
		coin %= coin_num[i];
		if (coin == 0)
			break;
	}
	cout << temp << endl;

	return 0;
}