#include <bits/stdc++.h>
#define MAX 20001
using namespace std;

int k, v, e;
int visited[MAX];
vector<int> g[MAX];

void dfs(int);
void init();
bool isGraphCheck();

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> k;
	while (k--) {
		cin >> v >> e;

		for (int i = 0; i < e; i++) {
			int a, b;
			cin >> a >> b;
			g[a].push_back(b);
			g[b].push_back(a);
		}

		for (int i = 1; i <= v; i++) {
			if (!visited[i]) {
				dfs(i);
			}
		}

		if (isGraphCheck()) cout << "YES\n";
		else cout << "NO\n";

		init();
	}
}

void dfs(int start) {
	if (!visited[start]) {
		visited[start] = 1;
	}

	for (int i = 0; i < g[start].size(); i++) {
		int next = g[start][i];
		if (!visited[next]) {
			if (visited[start] == 1) visited[next] = 2;
			else if (visited[start] == 2) visited[next] = 1;
			dfs(next);
		}
	}
}

bool isGraphCheck() {
	for (int i = 1; i <= v; i++) {
		for (int j = 0; j < g[i].size(); j++) {
			int next = g[i][j];
			if (visited[i] == visited[next]) {
				return false;
			}
		}
	}
	return true;
}

void init() {
	for (int i = 0; i <= v; i++) {
		g[i].clear();
		visited[i] = 0;
	}
}
