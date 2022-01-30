#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
    
	int n;
	cin>>n; 
	
	int A[n];
	for(int i = 0; i<n; i++) {
		cin>>A[i];
	}
	
	// 필요한 감독관의 최소 수는 최악의 경우 int형 표현 범위를 초과하므로
	// long long 형으로 선언. 
	long long int viewer = 0;
	int B, C;
	cin>>B>>C;
	for(int i = 0; i<n; i++) {
		// 시험장의 총감독관은 오직 1명 
		viewer++;
		// 총감독관이 감시할 수 있는 응시자 수를 뺀다. 
		A[i] -= B;
		
		// 0보다 큰 경우 같은 시험장에 부감독관이 감시할 수 있는 응시자 수를 계산한다. 
		if(A[i]>0) {
			viewer += A[i]%C > 0 ? A[i] / C + 1 : A[i] / C;
		} 
	} 
	// 각 시험장마다 응시생을 모두 감독하기 위한 필요 감독관의 최소 수 출력 
	cout<<viewer;
} 
