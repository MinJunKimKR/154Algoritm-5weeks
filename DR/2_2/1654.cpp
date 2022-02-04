#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {	
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
	int k, n;
	cin>>k>>n;
	
  vector<int> line(k);
	for(int i = 0; i <k; i++) {
		cin>>line[i];
	}
	sort(line.begin(), line.end());
	
	long long int start = 1, end = line[k-1];
	while(start<=end) {
		long long int mid = (start + end) / 2;
        
		int line_cnt = 0;
		for(int i = 0; i<k; i++) {
			line_cnt += line[i]/mid;
		}
		
		if(line_cnt >= n) {
			start = mid + 1;
		} else {
			end = mid - 1;
		}
	}
    cout<<end;
    return 0;
}
