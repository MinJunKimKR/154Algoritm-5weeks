#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{							
	ios::sync_with_stdio(false);
	cin.tie(0);	
	string s;
	int cnt = 0, default_cnt = 0;
	cin>>s;
	
	stack<char> s2;
	for(int i = 0; i<s.length(); i++) {
		if(s[i] == '(' && s[i+1] == ')') {
			if(!s2.empty()) {
				cnt+=s2.size(); 
			}
			i++;
		} else if(s[i] == '(') {
			s2.push(s[i]);
			default_cnt++; 
		} else if(s[i] == ')') {
			s2.pop(); 
		}
	}
	cout<<cnt + default_cnt;
	return 0;
} 
