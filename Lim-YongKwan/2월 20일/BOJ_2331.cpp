#include<iostream>
#include<math.h>

using namespace std;


int graph[300001];
bool visit[300001];

int main() {

	long long a, p;
	cin >> a >> p;

	long long temp = 0;
	visit[a] = 1;
	while (a > 0) {
		temp += pow((a % 10), p);
		a /= 10;
	}
	a = temp;
	
	
	int answer = 1;

	while (visit[temp] == 0) {
		
		if(graph[temp]==0) {
			graph[temp] = answer;
			visit[temp] = 1;
			temp = 0;
			while (a > 0) {
				temp += pow((a % 10), p);
				a /= 10;
			}
			a = temp;
		}
		else if (graph[temp] != 0) {
			break;
		}
		answer++;
	}

	cout << graph[temp] << endl;

	return 0;
}