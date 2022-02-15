#include <bits/stdc++.h>
#define MAX 26
using namespace std;

int n, dan_cnt;
int board[MAX][MAX];
int move_xy[4][2] = { {-1,0}, {1,0}, {0,-1}, {0,1} };
bool visited[MAX][MAX];
vector<int> v;

void dfs(int x, int y) {
	dan_cnt++;
	visited[x][y] = true;

	for (int w = 0; w < 4; w++) {
		int mx = x + move_xy[w][0];
		int my = y + move_xy[w][1];
		if (mx < 0 || my < 0 || mx >= n || my >= n) {
			continue;
		}

		if (board[mx][my] == 1 && !visited[mx][my]) {
			dfs(mx, my);
		}
	}
}

int main() {
	cin >> n;

	for (int i = 0; i < n; i++) {
		string row;
		cin >> row;
		for (int j = 0; j < n; j++) {
			board[i][j] = row[j] - '0';
		}
	}


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j] == 1 && !visited[i][j]) {
				dan_cnt = 0;
				dfs(i, j);
				v.push_back(dan_cnt);
			}
		}
	}


	sort(v.begin(), v.end());
	cout << v.size() << "\n";
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << "\n";
	}
	return 0;
}
