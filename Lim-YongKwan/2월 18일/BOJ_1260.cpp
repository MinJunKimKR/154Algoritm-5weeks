#include<iostream>
#include<cstring>
#include<queue>
#include<stack>

using namespace std;

int graph[1001][1001];
int n, m;

int visit[1001];

void BFS(queue<int>& v) {

	cout << v.front() << " ";
	int temp = v.front();
	v.pop();

	visit[temp] = 1;

	for (int i = 0; i <= n; i++) {
		if (graph[temp][i] == 1 and visit[i] == 0) {
			v.push(i);
			visit[i] = 1;
		}
	}

	if (v.size() > 0) {
		BFS(v);
	}

	return;
}

void DFS(stack<int>& v) {

	cout << v.top() << " ";
	int temp = v.top();
	v.pop();
	
	visit[temp] = 1;

	for (int i = 0; i <= n; i++) {
		if (graph[temp][i] == 1 and visit[i] == 0) {
			v.push(i);
			visit[i] = 1;
			DFS(v);
		}
	}

	if (v.size() > 0) {
		DFS(v);
	}

	return;
}

int main() {

	int v;
	cin >> n >> m >> v;
	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;
		graph[a][b] = 1;
		graph[b][a] = 1;
	}
	stack<int> first;
	queue<int> second;

	first.push(v);
	second.push(v);

	visit[v] = 1;
	DFS(first);
	cout << endl;

	memset(visit, 0, sizeof(visit));

	visit[v] = 1;
	BFS(second);

	return 0;
}