#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int k;
	while(1) {
		cin>>k;
		
		if(k == 0) break;
		
    		// 집합을 구성할 벡터와 6개의 원소를 뽑는데 구별할 lotto라는 벡터 선언
		vector<int> v(15);
		vector<int> lotto; 
		for(int i = 0; i<k; i++) {
			cin>>v[i];
		}
		
    		// 앞에부터 6개의 원소만 뽑을 것이므로 true 처리를 해주고, 이외 k-6개는 false 처리
		for(int i = 0; i<6; i++) {
			lotto.push_back(1);
		}
		for(int i = 0; i<k-6; i++) {
			lotto.push_back(0);
		}
		
	    	// lotto에 해당하는 값 중 true 처리가 된 것만 차례대로 출력을 해준 후,
	    	// prev_permutation을 이용해 현재 나와 있는 배열에서 인자로 넘어간 범위에 해당하는 이전 순열을 구하고 순열이 안나올때까지 구한다.
		do {
			for(int i = 0; i<k; i++) {
				if(lotto[i]) {
					cout<<v[i]<<' ';
				}
			}
			cout<<"\n";
		}while(prev_permutation(lotto.begin(), lotto.end()));
		
		cout<<"\n";
	}
} 
