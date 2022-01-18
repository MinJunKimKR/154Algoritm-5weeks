#include <iostream>

using namespace std;

long long int DP[91];
int n;

// 이친수는 0으로 시작하지 않는다.
// 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.

void pinary() {
	// 1, 10인 경우를 활용한다.
	DP[1] = 1;
	DP[2] = 1;

	// i자리 이친수가 DP[i]라고 하면 마지막 자릿 수가 0인 경우 앞에 0, 1 어떤 숫자든 상관이 없지만, 마지막 자릿 수가 1인 경우 앞에 0만 올 수 있다.
	// 따라서, 맨 마지막 자릿 수가 0이면 i-1 자릿 수가 앞에 올 수 있고, 1이면 01 앞에 i-2 자릿 수 가 오면 된다.
	for (int i = 3; i <= n; i++) 
		DP[i] = DP[i - 1] + DP[i - 2];

}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n;
	pinary();

	// n자리 이친수의 개수 출력
	cout << DP[n];
	return 0;
}
