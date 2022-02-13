#include<iostream>
#include<queue>
#define endl "\n"
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n, k;
	cin >> n >> k;

	queue<int> josephus;

	int temp;
	for (int i = 1; i <= n; i++) {
		temp = i;
		josephus.push(temp);
	}

	int circle = 1;
	cout << "<";
	while (josephus.size() > 0) {

		temp = josephus.front();
	//	cout << "Temp : " << temp << endl;
		josephus.pop();
		if(circle != k)
			josephus.push(temp);
		
		if (circle == k and josephus.size()>=1) {
			cout << temp<<", ";
			circle = 0;
		}
		else if (circle == k and josephus.size() < 1) {
			cout << temp << ">";
			circle = 0;
		}
		circle++;
	}



	return 0;
}