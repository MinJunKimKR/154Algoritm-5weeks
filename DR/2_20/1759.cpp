#include <bits/stdc++.h>
using namespace std;

int L, C;
vector<char> ch;
vector<char> str;

bool isPwd() {
	int cnt = 0;
	// 모음이 있다면 카운트
	for (int i = 0; i < L; i++) {
		if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' ||
			str[i] == 'o' || str[i] == 'u') {
			cnt++;
		}
	}
	// 모음이 1개 이상이면서 자음이 2개 이상일 경우 암호에 해당
	if (cnt >= 1 && L - cnt >= 2) return true;
	else return false;
}

void dfs(int s) {
	// 문자열의 길이가 L과 같다면 모음(최소 1개)과 자음의 수(최소 2개)를 체크하여 출력
	if (str.size() == L) {
		if (isPwd()) {
			for (int i = 0; i < L; i++) {
				cout << str[i];
			}
			cout << "\n";
		}
		return;
	}

	// 암호의 길이와 일치할 때까지 하나씩 넣어주고, 위의 조건문이 수행됐을 때 dfs가 종료되므로 하나씩 문자를 빼주면서
	// 이 과정을 반복해 가능한 암호를 모두 출력해준다.
	for (int i = s; i < C; i++) {
		str.push_back(ch[i]);
		dfs(i + 1);
		str.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	// 암호의 문자 수와 문자의 종류 입력
	cin >> L >> C;
	for (int i = 0; i < C; i++) {
		char tmp;
		cin >> tmp;
		ch.push_back(tmp);
	}
	
	// 암호는 오름차순으로 나열되어야 하므로 정렬 수행 후 DFS
	sort(ch.begin(), ch.end());
	dfs(0);
	return 0;
}
