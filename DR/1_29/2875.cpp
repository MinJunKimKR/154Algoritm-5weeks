#include <iostream>

using namespace std;

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	
	int n, m, k, team_cnt = 0;
	cin>>n>>m>>k;
	
	while(n>=2 && m>=1 && n+m-k>=3) {
		n-=2;
		m-=1;
		team_cnt++;
	}
	
	cout<<team_cnt;
	return 0;
} 
