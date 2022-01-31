#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int n, meet_cnt = 0;
	cin>>n;
	
	vector<pair<int, int>> v(n);
	for(int i = 0; i<n; i++) {
		cin>>v[i].second>>v[i].first;
	}
	
	sort(v.begin(), v.end());
	
	int s = 0;
	for(int i = 0; i<v.size(); i++) {
		if(s <= v[i].second) {
			s = v[i].first;
			meet_cnt++;
		}
	}
	
	cout<<meet_cnt;
	
    return 0;
}
