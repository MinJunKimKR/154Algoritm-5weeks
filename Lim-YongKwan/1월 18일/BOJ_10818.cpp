#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main() {

	int n;
	cin >> n;
	vector<int> element;
	int temp;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		element.push_back(temp);
	}
	cout<< *min_element(element.begin(), element.end())<<" "<<*max_element(element.begin(),element.end());

	return 0;
}