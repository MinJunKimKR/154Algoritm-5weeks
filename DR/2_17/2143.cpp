#include <bits/stdc++.h>
#define MAX 1001
using namespace std;

int T, n, m;
int A[MAX];
int B[MAX];
vector<int> A_sum, B_sum;

int main() {
	cin>>T;
	
	cin>>n;
	for(int i = 0; i<n; i++) {
		cin>>A[i];
	}
	
	cin>>m;
	for(int i = 0; i<m; i++) {
		cin>>B[i];
	}
	
	for(int i = 0; i<n; i++) {
		int sum = 0;
		for(int j = i; j<n; j++) {
			sum += A[j];
			A_sum.push_back(sum);	
		}
	}
	
	for(int i = 0; i<m; i++) {
		int sum = 0;
		for(int j = i; j<m; j++) {
			sum += B[j];
			B_sum.push_back(sum);	
		}
	}
	
	sort(A_sum.begin(), A_sum.end());
	sort(B_sum.begin(), B_sum.end());
	
	long long int answer = 0;
	for(int i = 0; i<A_sum.size(); i++) {
	    answer += upper_bound(B_sum.begin(), B_sum.end(), T - A_sum[i])
				- lower_bound(B_sum.begin(), B_sum.end(), T - A_sum[i]);
	}
	cout<<answer;
    return 0;
}
