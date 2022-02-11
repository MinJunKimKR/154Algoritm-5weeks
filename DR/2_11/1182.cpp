#include <iostream>
#include <vector>
#define MAX 21
using namespace std;

int n, s, sum, cnt;
vector<int> v(MAX);

void search(int i, int sum) {
	if(i == n) {
		// 끝까지 탐색 수행 후 구하고자 하는 부분수열 합과 같다면 카운트 
		if(sum == s) cnt++;
		return;
	}
	// 원소를 선택하는 경우와 선택하지 않는 경우 두가지로 나누어, 백트래킹을 적용
	// n번까지 탐색한 후 합이 s와 같았을 때만 카운트된다. 
	
	// 현재의 원소를 sum에 더하지 않는 경우 
	search(i+1, sum);
	
	// 현재의 원소를 sum에 더하는 경우 
	search(i+1, sum + v[i]);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>n>>s;
	
	for(int i = 0; i<n; i++) {
		cin>>v[i];
	}	
	
	// 벡터 내 첫번째 원소부터 탐색을 시작한다. 
	search(0, 0);
	
	// 구하고자 하는 부분수열 합이 0인 경우, 아무 원소도 선택하지 않았을 때는 제외 
	if(s==0) cnt--;
	cout<<cnt;
} 
