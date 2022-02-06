#include<iostream>
#include<algorithm>
#include<vector>
#define endl "\n"

using namespace std;

int main() {

	int n;
	cin >> n;

	int temp;

	vector<int> sequence;
	for (int i = 0; i < n; i++) {
		cin >> temp;
		sequence.push_back(temp);
	}

	vector<long long> DP;

	DP.push_back(sequence[0]); //DP[0]은 sequence[0]

	for (int i = 1; i < n; i++) { //시퀀스[0] 값은 들어가 있으니 1부터 시작.
		DP.push_back(sequence[i]); //해당 범위보다 작은 0값을 넣어주자 XXXXXXXXXXX 0을 넣으면 오류 발생(3, 105 31 104) 해당 시퀀스 값을 넣어주자. 
		for (int j = 0; j < i; j++) { //j는 순환해야 하니 0부터 i값 까지 돌리자.
			if (sequence[i] > sequence[j]) { //만일 현재 sequence 값이 이전의 sequecne 값보다 크다면
				if(DP[i] <= DP[j] + sequence[i]) //또한 DP 가 바뀔 DP보다 작다면
					DP[i] = DP[j] + sequence[i]; // DP 값 변경.
			}
		}
	}

	//for (int i = 0; i < n; i++) { // 디버깅 체크를 위한 출력문.
	//	cout << "DP : " << DP[i] << " ";
	//}
	//cout << endl;

	cout << *max_element(DP.begin(), DP.end()) << endl; //가장 큰 값 출력

	return 0;
}