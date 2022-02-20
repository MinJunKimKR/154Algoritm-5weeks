#include<iostream>
#include<queue>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

int block[26][26];
int visit[26][26];

int direction[4][2] = { {0,1},{1,0},{0,-1},{-1,0} };

void DFS(int total,int n,int x, int y) {
	
	if (total == 0) {
		cout << "total 소진... " << endl;
		return;
	}
	if (x == 0 or y == 0) {
		return;
	}
	if (x == n or y == n) {
		return;
	}
	if (visit[x][y] == 1) {
		return;
	}
	if (block[x][y] == 0){
		return;
	}
	visit[x][y] = 1;
	

	for (int i = 0; i < 4; i++) {
			if (block[x + direction[i][0]][y + direction[i][1]] == 1 and visit[x + direction[i][0]][y + direction[i][1]] == 0) {
				cout << "visit 성공 : " << x+direction[i][0] <<" "<<y+direction[i][1]<<endl;
				visit[x + direction[i][0]][y + direction[i][1]] = 1;
				total--;
				DFS(total,n,x+direction[i][0],y+direction[i][1]);
			}
		
	}

	return;
}

int main() {

	int n = 0;
	cin >> n;

	int total = 0;
	
	char temp;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> temp;
			block[i][j] = temp-'0';
			if (block[i][j] == 1) {
				total++;
			}
		}
	}

	int count = 0;
	vector<int> answer;
	int number = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (block[i][j] != 0 and visit[i][j] == 0) {
				cout << "DFS 시동 : " << endl;
				count++;
				DFS(total, n, i, j);
			}
		}
	}

	cout << count << endl;

	return 0;
}