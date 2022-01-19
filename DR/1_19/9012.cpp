#include <iostream>
#include <string>
#include <stack>

using namespace std;

int check_bracket(string sen);

int main() {
	int t;
	string brac_sen;
	cin>>t;
	for(int i = 0; i<t; i++) {
		cin>>brac_sen;
		if(check_bracket(brac_sen) == 1) {
			cout<<"YES"<<endl;
		}
		else {
			cout<<"NO"<<endl;
		}
	}

	return 0;
}

// 괄호 검사 알고리즘 
int check_bracket(string sen) {
	stack<char> s;
	char ch;
	int n = (int)sen.length();
	
	for(int i = 0; i<n; i++) {
		ch = sen[i];
		switch(ch) {
			case '(':
				s.push(ch);
				break;
			case ')':
				if(s.empty()) {
					return 0;
				}
				else {
					s.pop();
				}
				break;
		}
	}
	if(!s.empty()) {
		return 0;
	}
	return 1;
}
