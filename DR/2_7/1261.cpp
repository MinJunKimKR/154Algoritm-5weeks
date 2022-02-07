#include <iostream>
#include <queue>
#include <string>
#define MAX 101
#define INF 999999999
using namespace std;

int n, m;
int maze[MAX][MAX];
int dist[MAX][MAX];
int move_xy[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

void move_bfs() {
	queue<pair<int, int> > q;
	q.push({0,0});
	dist[0][0] = 0;
	
	while(!q.empty()) {
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		
		for(int w = 0; w<4; w++) {
			int mx = x + move_xy[w][0];
			int my = y + move_xy[w][1];
			if(mx<0 || my<0 || mx>=m || my>=n) {
				continue;
			} 
			
			if(maze[mx][my]) {
				if(dist[mx][my] > dist[x][y] + 1) {
					dist[mx][my] = dist[x][y] + 1;
					q.push({mx, my});
				}
			} else if(!maze[mx][my]) {
				if(dist[mx][my] > dist[x][y]) {
					dist[mx][my] = dist[x][y];
					q.push({mx, my});
				}
			}
		}
	}
	
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	cin>>n>>m;
	
	string str;
	for(int i = 0; i<m; i++) {
		cin>>str;
		for(int j = 0; j<n; j++) {
			dist[i][j] = INF;
			maze[i][j] = str[j] - '0';
		}
	}
	
	move_bfs();
	cout<<dist[m-1][n-1];
} 
