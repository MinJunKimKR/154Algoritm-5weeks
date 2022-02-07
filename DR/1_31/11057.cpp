#include <iostream>
#define MAX 1001
#define MOD 10007
using namespace std;

// N의 범위가 1~1000이므로 MAX는 1001인 DP 배열과 오르막 수를 대입할 변수 선언 
int DP[MAX][10], result;

int main(void) {
	int n;
	cin>>n;
	
	// 1자리일 때는 0~9까지 경우의 수는 1가지 
	for(int i = 0; i<=9; i++) {
		DP[1][i] = 1;
	}
	
	// 2자리부터 앞에 올 수 있는 수를 카운트했을 때 
	// 오르막 수는 i-1 자리에서 0부터 j까지 오는 경우를 계산하면 된다. 
	for(int i = 2; i<=n; i++) {
		for(int j = 0; j<=9; j++) {
			for(int k = 0; k<=j; k++) {
				DP[i][j] = (DP[i][j] + DP[i-1][k])%MOD;		
			}
		}
	}
	
	// 길이가 n인 오르막 수의 개수를 구한다. 
	for(int i = 0; i<=9; i++) {
		result += DP[n][i];
	}
	
	cout<<result%MOD;
    return 0;
}
