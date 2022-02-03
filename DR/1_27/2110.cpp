#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n, c, max_dist = 0;
	cin>>n>>c;
	
	vector<int> v(n);
	for(int i = 0; i<n; i++) {
		cin>>v[i];
	}
	
	sort(v.begin(), v.end());
	
	int start = 0, end = v[n-1], ip_cnt;
	while(start<=end) {
		int mid = (start + end) / 2, ip_cnt = 1;
		int prev = v[0];
		for(int i = 1; i<n; i++) { 
			if(v[i] - prev >= mid) {
				prev = v[i];
				ip_cnt++;
			} 
		}
		if(ip_cnt >= c) {
			start = mid + 1;
			max_dist = max(max_dist, mid);
		} else {
			end = mid - 1;
		}
	}
	cout<<max_dist;
}
