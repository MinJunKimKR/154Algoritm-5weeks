#include <iostream>
#include <algorithm>
#include <stdlib.h>
using namespace std;

bool cmp(int a, int b) {
	return a < b;
}

int main() {
	int n, k;
	scanf("%d %d",&n ,&k);
	int* arr = new int[n];
	for(int i = 0; i<n; i++) {
		scanf("%d",&arr[i]);
	}
	sort(arr, arr+n, cmp);
	printf("%d",arr[k-1]);
	
	delete[] arr;
}
