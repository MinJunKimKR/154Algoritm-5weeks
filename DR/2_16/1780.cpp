#include <bits/stdc++.h>
#define MAX 2190
using namespace std;

int n;
int mat[MAX][MAX];
int cnt[3];

// 종이가 모두 같은 수인지 체크
bool isSame(int x, int y, int n) {
	int check = mat[x][y];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (mat[x + i][y + j] != check) return false;
		}
	}
	return true;
}

void paperCheck(int x, int y, int n) {
	// 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용하고 카운트한다.
	if (isSame(x, y, n)) {
		int cnt_num = mat[x][y];
		cnt[cnt_num + 1]++;
		return;
	}

	// 모두 같지 않은 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 아래의 과정을 반복한다.
	int divide = n / 3;
	for(int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			paperCheck(x + divide*i, y + divide * j, divide);
		}
	}

}

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> mat[i][j];
		}
	}

	// n*n 에서 0,0부터 시작해 종이의 개수를 체크한다.
	paperCheck(0, 0, n);

	// -1, 0, 1로 채워진 종이의 개수를 각각 출력
	for (int i = 0; i < 3; i++) {
		cout << cnt[i] << "\n";
	}
}
