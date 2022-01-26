#include <iostream>

using namespace std;

int n, m, u, v;
int visited[1001];
int arr[1001][1001];

void dfs(int x) {
	visited[x] = true;
	for(int i = 1; i<=n; i++) {
		if(arr[x][i] == 1 && visited[i] == 0) {
			dfs(i);
		}
	}
}

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin>>n>>m; 
	for(int i = 0; i<m; i++) {
		cin>>u>>v;
		arr[u][v] = 1;
		arr[v][u] = 1;
	}
	
	int cnt = 0;
	for(int i = 1; i<=n; i++) {
		if(!visited[i]) {
			cnt++;	
		}
		dfs(i);
	}
	cout<<cnt;
	return 0;
} 
