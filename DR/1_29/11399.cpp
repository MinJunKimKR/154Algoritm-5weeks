#include <iostream>
#include <algorithm>
#define MAX 1000
using namespace std;

int cmp(int a, int b) {
	return a < b;
}

int main(void) {
	int n, P[MAX] = {0}, sum = 0;
	cin>>n;
	for(int i = 0; i<n; i++) {
		cin>>P[i];
	}
	
	sort(P, P+n, cmp);
	for(int i = 0; i<n; i++) {
		if(i!=0) {
			P[i] = P[i-1] + P[i];
		} 
		sum += P[i];
	}
	cout<<sum;
	
    return 0;
}
