#include <bits/stdc++.h>
#define MAX 50
using namespace std;

int w, h, cnt;
int Island[MAX][MAX];
int move_xy[8][2] = { {-1,0}, {1,0}, {0,-1}, {0,1},
					{-1,-1}, {-1,1}, {1,1}, {1,-1} };
bool visited[MAX][MAX];

void dfs(int h, int w) {
	visited[h][w] = true;
  
  	// 대각선에 있는 좌표까지 고려하므로 총 8개의 좌표이고, 최대 지도 범위를 넘지 않는 선에서 DFS를 수행
	for (int m = 0; m < 8; m++) {
		int mh = h + move_xy[m][0];
		int mw = w + move_xy[m][1];

		if (mh >= 0 && mw >= 0 && mh < MAX && mw < MAX) {
			if (Island[mh][mw] == 1 && !visited[mh][mw]) {
				dfs(mh, mw);
			}
		}
	}
}

void init() {
	cnt = 0;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			Island[i][j] = 0;
			visited[i][j] = false;
		}
	}
}

int main() {

	while (1) {
    		// 지도의 너비와 높이 입력
		cin >> w >> h;
		if (w == 0 && h == 0) break;
    
    		// 테스트 케이스별로 수행되므로 매번 초기화 후, 지도 입력
		init();
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> Island[i][j];
			}
		}
    
    		// 섬이 존재하면서, 방문처리되지 않은 경우 DFS 수행하여 지도에 있는 섬의 개수 카운트
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (Island[i][j] == 1 && !visited[i][j]) {
					dfs(i, j);
					cnt++;
				}
			}
		}

		cout << cnt << "\n";
	}


	return 0;
}
