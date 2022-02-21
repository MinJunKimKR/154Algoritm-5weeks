#include <bits/stdc++.h>
#define MAX 21
using namespace std;

int R, C, result;
int alpha[MAX][MAX];
bool visited[26];
int move_xy[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

void dfs(int x, int y, int cnt) {
	result = max(result, cnt);
	
	for(int w = 0; w<4; w++) {
		int mx = x + move_xy[w][0];
		int my = y + move_xy[w][1];
		if(mx>=0 && my>=0 && mx<R && my<C) {
			if(!visited[alpha[mx][my]]) {
				visited[alpha[mx][my]] = true;
				dfs(mx, my, cnt + 1);
				visited[alpha[mx][my]] = false;
			}
		}
		
	}
}


int main() {
	cin>>R>>C;
	for(int i = 0; i<R; i++) {
		string row;
		cin>>row;
		for(int j = 0; j<C; j++) {
			alpha[i][j] = row[j] - 'A';
		}
	}
	
	visited[alpha[0][0]] = true;
	dfs(0, 0, 1);
	cout<<result;
    return 0;
}
