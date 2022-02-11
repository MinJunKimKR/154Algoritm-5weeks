#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	// 수열의 길이 n과 부분합이 되는 기준 s 입력 
	int n, s;
	cin>>n>>s;
	
	// 수열에 대한 데이터 입력 
	int A[n];
	for(int i = 0; i<n; i++) {
		cin>>A[i];
	}
	
	// 투포인터를 위한 변수와 최소 길이, 부분합을 나타내는 변수 선언
	// n의 범위가 100,000까지 이므로 기존 이중 반복문 풀이로는 O(N^2)에 시간초과 
	int left = 0, right = 0, min_len = 100001, sum = 0;
	while(1) {
		// 부분합이 s보다 크거나 같은 경우 기존 길이와 투 포인터의 위치를 빼준 것의 길이를
		// 비교해 짧은 것의 길이를 구해준 후, left에 해당하는 데이터는 하나씩 빼준다. 
		if(sum >= s) {
			min_len = min(min_len, right - left);
			sum -= A[left++];
		} 
		// right가 수열의 길이 n과 같아진다면 수열의 끝에 도달했다는 의미로 반복문 종료 
		else if(right == n) {
			break;
		}
		// 이외 부분합이 s보다 작은 경우엔 계속 right에 해당하는 데이터를 더해주면서 위치를 앞으로 이동한다. 
		else {
			sum+=A[right++];
		}
	}
	// 연속된 수들의 부분합 중 합이 S이상이 되는 기준에서 가장 짧은 것의 길이 출력
	// 합을 만드는 게 불가능하다면 0 출력 
	if(min_len == 100001) {
		cout<<0;
	} else {
		cout<<min_len;	
	}
} 
