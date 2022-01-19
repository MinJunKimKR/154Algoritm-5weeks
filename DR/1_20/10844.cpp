#include <iostream>
#define MAX 101
#define MOD 1000000000
using namespace std;

int n;
// 최대 자릿 수가 100까지이므로 int형의 표현 범위를 초과한다.
// 따라서, long long 형으로 선언해줘야 한다. 
long long int DP[MAX][11], cnt;

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	 
	cout.tie(0);
	
	cin>>n;
	
	// 길이가 i일 때, 마지막 수가 j인 경우 계단의 수 => DP[i][j]
	DP[1][0] = 0; // 1일 때 수가 0이라면 계단의 수는 0이다. 
	for(int i = 1; i<=9; i++) {
		DP[1][i] = 1; // 0 제외 한자리 수는 모두 계단 수 
	}
	
	// 길이가 2이상일때부터 계단 수를 구하는데 규칙이 있다. 
	for(int i = 2; i<=n; i++) {
		for(int j = 0; j<=9; j++) {
			// i일 때, 마지막 수가 0인 경우 전에 1밖에 오지못한다.
			// 마지막 수가 9인 경우에도 8밖에 오지못한다. 
			// 이외 길이가 i일 때 마지막 수가 j인 경우 그 전 자리에, j+1 또는 j-1의 계단 수가 온다. 
			if(j==0) DP[i][j] = DP[i-1][j+1] % MOD;
			else if(j==9) DP[i][j] = DP[i-1][j-1] % MOD;
			else DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % MOD;
		}
	}
	
	// 길이가 n인 계단 수가 총 몇개 있는지 카운트한다. 
	for(int i = 0; i<=9; i++) {
		cnt += DP[n][i];
	}
	
	cout<<cnt%MOD;
	return 0;
} 
