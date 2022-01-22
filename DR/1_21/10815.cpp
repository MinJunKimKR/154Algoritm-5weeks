#include <iostream>
#include <algorithm>
using namespace std;

int search(int arr[], int length, int target) { // 반복적 
	int start = 0;
	int end = length-1;
	int mid;
	
	while(start<=end) {
		mid = (start+end)/2;
		if(arr[mid] == target) {
			return mid;
		} else {
			if(arr[mid] > target) {
				end = mid-1;
			} else {
				start = mid+1;
			}
		}
	}
	return -1;
}

bool cmp(int a, int b) {
	return a<b;
}

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	 
	int n, m, result;
	cin>>n;
	
	int store[n];
	for(int i = 0; i<n; i++) {
		cin>>store[i];
	}
	sort(store, store+n, cmp);
	
	cin>>m;
	int custom[m];
	for(int i = 0; i<m; i++) {
		cin>>custom[i];
	}
	
	for(int i = 0; i<m; i++) { 
		result = search(store, n, custom[i]);
		if(result==-1) {
			cout<<0<<' ';
		} else {
			cout<<1<<' ';
		}
	}
	return 0;
}
