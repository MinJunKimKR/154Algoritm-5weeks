#include <bits/stdc++.h>
#define MAX 100001
using namespace std;

int n, k, result;
bool visited[MAX];
queue<pair<int, int> > qt;

int main() {
	cin >> n >> k;

	qt.emplace(n, 0);

	while (!qt.empty()) {
		int locate = qt.front().first;
		int t = qt.front().second;
		qt.pop();

		if (locate == k) {
			result = t;
			break;
		}

		int m1 = locate - 1;
		int m2 = locate + 1;
		int m3 = 2 * locate;

		if (m1 >= 0 && !visited[m1]) {
			visited[m1] = true;
			qt.emplace(m1, t + 1);
		}

		if (m2 <= k && !visited[m2]) {
			visited[m2] = true;
			qt.emplace(m2, t + 1);
		}

		if (m3 <= k + 1 && !visited[m3]) {
			visited[m3] = true;
			qt.emplace(m3, t + 1);
		}

	}

	cout << result;
	return 0;
}
