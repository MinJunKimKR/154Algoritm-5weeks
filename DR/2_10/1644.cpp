#include <iostream>
#include <cmath>
#include <vector>
#define MAX 4000001
using namespace std;

int n, prime_cnt = 0, sum = 0;
bool arr[MAX];
vector<int> v;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>n;
  
	for(int i = 2; i<sqrt(MAX); i++) {
		if(!arr[i]) {
			for(int j = 2*i; j<=MAX; j+=i) {
				arr[j] = true;
			}
		}
	}

	for(int i = 2; i<=n; i++) {
		if(!arr[i]) {
			v.push_back(i);
		}
	}

	int left = 0, right = 0;
	while(1) {
		if(sum >= n) {
			if(sum == n) prime_cnt++;
			sum -= v[left++];
		} 
		else if(right == v.size()) {
			break;
		}
		else {
			sum += v[right++];
		}
	}
	cout<<prime_cnt;

} 
