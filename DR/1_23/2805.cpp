#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int n, m, result;
vector<int> tree;

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	 

	cin>>n>>m;
	for(int i = 0; i<n; i++) {
		int data;
		cin>>data;
		tree.push_back(data);
	}
	
	// 이분탐색을 위한 벡터 정렬 수행 
    sort(tree.begin(), tree.end());
    
    // start, end의 범위는 0부터 입력한 데이터의 가장 큰 값까지 해준다. 
	int start = 0, end = tree[n-1], mid;
	while(start <= end) {
		// 높이의 범위가 10억 이하이므로 더했을 때 int 유효범위를 초과하기에
		// long long int형으로 선언해주어야 한다. 
		long long int sum = 0;
		mid = (start + end) / 2;
		for(int i = 0; i<n; i++) {
			// 높이가 mid보다 큰 나무는 mid 위의 부분이 잘려 sum에 더해진다. 
			if(tree[i]>mid) {
				sum += tree[i] - mid;
			}
		}
		// m미터의 나무가 sum보다 큰 경우 end가 mid에서 하나 줄여 범위를 좁힌다. 
		if(sum < m) {
			end = mid - 1;	
		} // m미터의 나무가 sum보다 작거나 같은 경우 mid에서 1 증가시켜 범위를 좁히고, 이때의 mid값은 result에 대입한다. 
	 	else {
	 		result = mid;
			start = mid + 1;
		}
	}
	cout<<result;
	return 0; 
} 
