#include<iostream>
#include<queue>
#define endl "\n"

using namespace std;

int component[1001][1001];
int visit[1001];

void BFS(queue<int> v,int n) {

	int temp = v.front();
	v.pop();
	visit[temp] = 1;

	for (int i = 1; i <= n; i++) {
		if (visit[i] == 0 and component[temp][i] == 1) {
			v.push(i);
			visit[i] = 1;
		}
	}
	if (v.size() > 0) {
		BFS(v, n);
	}
	return;
}

int main() {

	int n, m;
	cin >> n >> m;
	
	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		component[a][b] = 1;
		component[b][a] = 1;
	}

	int count = 0;
	queue<int> v;
	for (int i = 1; i <= n; i++) {
		if (visit[i] == 0) {
			v.push(i);
			BFS(v,n);
			count++;
		}
	}

	cout << count << endl;

	return 0;
}