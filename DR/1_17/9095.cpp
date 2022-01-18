#include <iostream>
using namespace std;

// 테스트 케이스 변수 t와 경우의 수를 구하고자 하는 변수 n
int t, n;

int partition() {
	// n이 3이하일 때까지의 패턴을 구하고, 경우의 수를 배열에 저장해준다. 
	if(n<=3) {
		int dp[3] = {1, 2, 4}; 
		
		// dp[0]부터 시작하므로 n-1 위치의 값을 반환. 
		return dp[n-1];
	} else {
		// n=3까지의 경우의 수를 넣어놓고 n이 4일때부터 저장해놓은 값을 이용한다. 
		int dp[n] = {1, 2, 4};
		for(int i = 3; i<n; i++) {
			dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
		}
		return dp[n-1];
	}
	
}

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	 

	cin>>t;
	for(int i = 0; i<t; i++) {
		cin>>n;
		cout<<partition()<<endl;
	}

	return 0;
} 
