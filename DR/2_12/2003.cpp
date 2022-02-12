#include <iostream>

using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int n, m;
	cin>>n>>m; 
	
	int A[n], cnt = 0;
	for(int i = 0; i<n; i++) {
		cin>>A[i];
	}
	
	int sum = 0;
	for(int i = 0; i<n; i++) {
		sum = A[i];
		if(sum == m) {
			cnt++; continue;
		}
		for(int j = i+1; j<n; j++) {
			sum += A[j];
			
			if(sum == m) {
				cnt++; break;
			} else if(sum > m) {
				break;
			}
		}
	}
	cout<<cnt;
} 
