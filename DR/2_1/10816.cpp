#include <iostream>
#include <algorithm>
using namespace std;

bool cmp(int a, int b) {
	return a<b;
}

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	 
	int n, m, result, lower, upper;
	cin>>n;
	
	int mycard[n];
	for(int i = 0; i<n; i++) {
		cin>>mycard[i];
	}
    // 이분탐색이므로 정렬 수행
	sort(mycard, mycard+n, cmp);
	
    // m개의 카드를 담을 배열에 데이터 입력
	cin>>m;
	int check_card[m];
	for(int i = 0; i<m; i++) {
		cin>>check_card[i];
	}
	
	for(int i = 0; i<m; i++) { 
        // upper_bound는 찾고자 하는 값보다 큰 값이 처음으로 나타나는 위치이며,
        // lower_bound는 찾고자 하는 값 이상이 처음 나타나는 위치로써 
        // 두 값을 빼주면 해당 카드가 n개에서 몇 개 존재하는지 알 수 있다. 
		result = upper_bound(mycard, mycard+n, check_card[i]) - lower_bound(mycard, mycard+n, check_card[i]);
		cout<<result<<' ';
	}
	return 0;
}
