#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(int a, int b) {
	return a < b;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);	
	int n, m, res_size, i;
	cin>>n>>m;
	
	res_size = n+m;
	int A[n], B[m], C[res_size];
	for(i = 0; i<n; i++) {
		cin>>A[i];
		C[i] = A[i];
	}
	
	for(int j = 0; j<m; j++) {
		cin>>B[j];
		C[i+j] = B[j];
	}
	
	sort(C, C+res_size, cmp);
	for(int i = 0; i<res_size; i++) {
		cout<<C[i]<<' ';
	}
	
	return 0;
}
