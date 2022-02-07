#include <iostream>

using namespace std;

void stars(int n, int i, int j) {
	if((i/n)%3==1 && (j/n)%3==1) {
		cout<<" ";
	} else if(n/3 == 0) {
		cout<<"*";
	} else {
		stars(n/3, i, j);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n;
	cin>>n;
	
	for(int i = 0; i<n; i++) {
		for(int j = 0; j<n; j++) {
			stars(n, i, j);
		}
		cout<<"\n";
	}
	return 0;
}
