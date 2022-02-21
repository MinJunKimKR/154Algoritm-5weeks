#include<iostream>
#include<queue>
#include<stack>
#include<algorithm>
#include<cstring>
#include<vector>

#define endl "\n"

using namespace std;

bool visit[1001];
int graph[1001];

void BFS(int n) {
	visit[n] = 1;

	if (visit[graph[n]] == 0) {
		BFS(graph[n]);
	}

	return;
}

int main() {

	int testcase;
	cin >> testcase;
	while (testcase--) {

		memset(visit, 0, sizeof(visit));
		memset(graph, 0, sizeof(graph));

		int n;
		cin >> n;

		for (int i = 1; i <= n; i++) {
			cin >> graph[i];
		}
		int answer = 0;
		for (int i = 1; i <= n; i++) {
			if (visit[i] == 0) {
				BFS(i);
				answer++;
			}
		}

		cout << answer << endl;
	}

	return 0;
}