#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define MAX 41
using namespace std;

int n, s, mid;
long long int cnt;
vector<int> v(MAX);
map<int, int> m; 

void left_sum(int i, int sum) {
	// 부분 수열의 합이 sum일 때, 왼쪽 구간을 탐색하며 sum이 몇 번 나왔는지 카운트
	if (i == mid) {
		m[sum]++; 
		return;
	}

	left_sum(i + 1, sum);
	left_sum(i + 1, sum + v[i]);
}

void right_sum(int i, int sum) {
	// 오른쪽 구간에서의 부분 수열의 합을 구하고, n을 도달했을 시 m[s-sum]이 존재한다면 왼쪽 구간에서 구한 sum과
	// 오른쪽 구간에서의 sum을 더하면 S가 된다는 의미이므로 이때 부분수열 개수를 카운트
	if (i == n) {
		cnt += m[s - sum];
		return;
	}

	right_sum(i + 1, sum);
	right_sum(i + 1, sum + v[i]);
}

int main(void) {
	// 정수의 개수 n과 합 s 입력
	cin >> n >> s;
	mid = n / 2;
	for (int i = 0; i < n; i++) cin >> v[i];

	// N의 범위가 1~40이므로 O(2^N) 시간초과가 나기에 왼쪽과 오른쪽으로 나누어 모든 부분집합의 합을 구해주며, 이때 시간복잡도는 O(2^n/2)
	left_sum(0, 0);
	right_sum(mid, 0);

	// 구할 합이 0인 경우 모두 선택하지 않았을 때를 고려해 카운트를 제외시키고,
	// 합이 s가 되는 부분수열의 개수를 출력한다.
	if (s == 0) cnt--;
	cout << cnt;
	return 0;
}
