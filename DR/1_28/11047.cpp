#include <iostream>

using namespace std;

int main() {
	int n, k, cnt = 0;
	cin>>n>>k;
	
	int coin[n];
	for(int i = 0; i<n; i++) {
		cin>>coin[i];
	}
	 
	for(int i = n-1; i>=0; i--) {
		cnt += k / coin[i]; 
		k%=coin[i]; 
	}
	cout<<cnt;
}
